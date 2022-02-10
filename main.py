# add local PATH
import os
gtkhome = "C:\\Program Files\\GTK3-Runtime Win64\\bin"
os.environ["PATH"] = gtkhome + ";" + os.environ["PATH"]

# import libraries
from generator import inst2list, generate_metadata, offchain_metadata
from tqdm import tqdm

# clear terminal
os.system("cls")

# import XML tree library
from xml.etree import ElementTree as ET
import cairosvg

# exclude the namespace
ET.register_namespace("","http://www.w3.org/2000/svg")

# read the svg file
svg_filename = "./source/ganesha.svg"
tree = ET.parse(open(svg_filename,"r"))
root = tree.getroot()

# specify the project name
project_name = "./results/"+input("Project Name: ")
filename = project_name + "/{:04d}.png"
if not os.path.exists(project_name):
    os.mkdir(project_name)

project = {
    "index": "",
    "dir": project_name,
    "name": "",
    "description": "Ganesha is a collection of 7,777 generative arts inspired by one of the best most worshipped deities in the Hindu pantheon.",
    "image": "",
}
    
total = int(input("How many metadata you want?: "))
metadata = generate_metadata(total)

# iterate the metadata
for i in tqdm(range(total),"Generating the Ganesha"):
    instance = inst2list(metadata[i])

    # label filtering process
    for element in root.iter():
        if element.tag.split("}")[-1] == "g":
            label = element.get("{http://www.inkscape.org/namespaces/inkscape}label")
            style = element.get("style")
            if label in instance:
                new_style = style.replace("display:none","display:inline")
            else:
                new_style = style.replace("display:inline","display:none")
            element.set("style",new_style)

    # save the export candidate svg file
    tree.write("./source/exported.svg",xml_declaration=True)

    # export the svg into png
    cairosvg.svg2png(url="./source/exported.svg", write_to=filename.format(i+1))

    # assign the project information
    project['index'] = i+1
    project['image'] = filename.format(i+1)
    project['name'] = "Ganesha #{}".format(i+1)
    offchain_metadata(project,metadata[i])