import os
import xml.etree.ElementTree as ET

xml_header = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"

def CreateElementFile(element, directory):
    title = element.find('Name').text
    filename = format(title + ".xml")    
    if not os.path.exists(directory):
        os.makedirs(directory)
        file_with_path = os.path.join(directory, filename)
        with open(file_with_path, 'wb') as f:
            f.write(xml_header)
            f.write(ET.tostring(element))

# Explore the xml file for entities
# Divide them to folders by type
context = ET.iterparse('FILE.xml', events=("start", "end"))
for event, element in context:
    if element.tag == 'Entity':
        entity_type = element.find('Type').text
        directory = format("./Output/" + entity_type)
        CreateElementFile(element, directory)       
    elif element.tag == 'DeviceType':   
        directory = format("./Output/DeviceTypes/") 
        CreateElementFile(element, directory)   