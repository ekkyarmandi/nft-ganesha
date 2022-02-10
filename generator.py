# import necessary libraries
import json
import random

def gold_counter(metadata):
    '''
    Gold Body attribute counter.
    :param metadata: list with dict; metadata with attribtues value.
    :return count: int; total gold body attributes inside the metadata.
    '''
    count = 0
    for instance in metadata:
        if instance['BODY'] == 'GOLD':
            count += 1
    return count

def inst2list(instance):
    metadata = []
    for key,value in instance.items():
        if type(value) == list:
            for val in value:
                val = "_".join([key,val])
                metadata.append(val)
        else:
            val = "_".join([key,value])
            metadata.append(val)
    return metadata

def inst2str(instance):
    '''
    Convert instance/model variable into one single string.
    :param instance: dict; instance/model variable.
    :return instance_string: str; instance in one single string format.
    '''
    attributes = []
    for value in instance.values():
        if type(value) == list:
            for v in value:
                attributes.append(v)
        else:
            attributes.append(value)
    return ",".join(attributes)

def offchain_metadata(project,instance):
    project_dir = project['dir'] + "/" + f"{project['index']:04d}.json"
    metadata = {
        "name": project['name'],
        "description": project['description'],
        "image": project['image'],
        "external_url": "https://example.com",
        "attributes": []
    }
    for key,value in instance.items():
        if "ACCESSORIES" in key:
            prefix = key.replace("ACCESSORIES","")
            key = " ".join([prefix,"ACCESSORIES"])
        elif "ATTACHMENTS" in key:
            prefix = key.replace("ATTACHMENTS","")
            key = " ".join([prefix,"ATTACHMENTS"])
        key = key.title().strip()
        if value != "EMPTY":
            if type(value) == list:
                for val in value:
                    item = {
                        "trait_type": key,
                        "value": val.title()
                    }
            else:
                item = {
                    "trait_type": key,
                    "value": value.title()
                }
            metadata['attributes'].append(item)
    json.dump(metadata,open(project_dir,"w"),indent=4)

def random_generate(attributes):
    '''
    Metadata attributes random generator.
    :param attributes: dict; attributes/traits value.
    :return instance: dict; combination model.
    '''
    instance = {}
    for key in attributes:
        if key == "ACCESSORIES":
            n = len(attributes[key])
            k = random.randint(1,n)
            items = random.choices(attributes[key],k=k)
            items = list(dict.fromkeys(sorted(items)))
        else:
            items = random.choice(attributes[key])
        instance.update({key:items})
    return instance

def generate_metadata(total_instance=7777):
    '''
    Generating metadata in `total_instance`.
    :param total_distance: int; number of metadata will be generated.
    :return metadata: list; variable contains N instance combination/metadata.
    '''
    metadata = []
    metadata_strings = []
    attributes = json.load(open("./data/attributes.json"))
    while len(metadata_strings) < total_instance:

        # model random generation
        instance = random_generate(attributes)

        # exlcusion rules
        if instance['BODY'] == "GOLD":
            instance['ACCESSORIES'] = ["CLOVER"]
            gold_limit = 77 - gold_counter(metadata)

            # output for rule3 are the reverse value of itself, it adapt to rule1 and rule2
            if gold_limit > 0:
                rule3 = False # means allowed
            else:
                rule3 = True # means not allowed
        else:
            rule3 = False # means allowed

        # accessories rules
        rule1 = instance['BODYATTACHEMENTS'] == "HOLYTATTOO" and instance['LOWERATTACHMENTS'] == "BLACKPANTS"
        rule2 = instance['BODYATTACHEMENTS'] == "BLACKLONGTSHIRTS" and 'ARMACC' in ",".join(instance['ACCESSORIES'])

        # accept the folder
        if not any([rule1,rule2,rule3]):
            instance_string = inst2str(instance)
            if instance_string not in metadata_strings:
                metadata.append(instance)
                metadata_strings.append(instance_string)
    
    return metadata

if __name__ == "__main__":

    project_name = "test"
    metadata = generate_metadata(10)
    json.dump(metadata,open(f"./result/{project_name}.json","w"))