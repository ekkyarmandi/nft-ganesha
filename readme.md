# Ganesha Random Ganerative NFT

In this project me and [Hairil](https://www.upwork.com/o/profiles/users/~015df8753e642d5799/) (as the artist) works in team to produce 7,777 collection of Ganesha for NFT purpose.

I use Inkscape as the drawing software and python programming language with xml tree module, cairosvg, and gtk3 runtime software to do random generate artworks and exporting the svg file as an png.

## How to Run the Script
First make sure you have GTK3 installed on your machine. Secondly, add or specify the gtk local path into the main.py (you can look it at the [main.py](main.py) script).
```python
gtkhome = "C:\\Program Files\\GTK3-Runtime Win64\\bin"
os.environ["PATH"] = gtkhome + ";" + os.environ["PATH"]
```
After that you can run the main script by executing.
```
python main.py
```

You will be asking for the project name and numbers of artworks you wanted to generate.
```
Project Name: <name of the project folder, for exmaple: Ganesha>
How many metadata you want?: <number of should be generate metadata, for example: 7777>
```

The output will shown in [results](results/) folder including the png file and its metadata.

## Generated Example
<img src="./static/compilation.png">
