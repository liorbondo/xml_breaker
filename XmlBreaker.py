import xml.etree.ElementTree as ET

class XmlBreaker(object):
    def __init__(self, filename)
        self.filename = filename
        self.xmlContex = ET.iterparse(filename, events=("start", "end"))

    def set_directories(self, directories)
        self.directories = directories

    def break_xml()
        # Explore the xml file for entities
        # Divide them to folders by type
        for event, element in xmlContex:
            if element.tag == directories:
                entity_type = element.find('Type').text
                directory = format("./Output/" + entity_type)
                CreateElementFile(element, directory)       
            elif element.tag == 'DeviceType':   
                directory = format("./Output/DeviceTypes/") 
                CreateElementFile(element, directory)   

