import os
import xml.etree.ElementTree as ET

root_dir = "./Output/"
entities_dir = format(root_dir + "Entities/")

def SetTags(dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

def CreateElementFile(element, directory):
    title = element.find('Name').text
    filename = format(title + ".xml")    
    CreateDirectory(directory)
    file_with_path = os.path.join(directory, filename)
    with open(file_with_path, 'wb') as f:
        f.write(ET.tostring(element))

#Create Entities folder
CreateDirectory(entities_dir)

# Explore the xml file for entities
# Divide them to folders by type
context = ET.iterparse('FILE.xml', events=("start", "end"))
for event, element in context:
    if element.tag == 'Entity':
        entity_type = element.find('Type').text
        directory = format(entities_dir + entity_type)
        CreateElementFile(element, directory)       
    elif element.tag == 'DeviceType':   
        directory = format(root_dir + "DeviceTypes") 
        CreateElementFile(element, directory)   