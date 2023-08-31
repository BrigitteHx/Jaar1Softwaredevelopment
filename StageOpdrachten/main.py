from xmlschema import XMLSchema
from xml.etree import ElementTree as ET

# Laden XSD-schema
xsd = XMLSchema('example.xsd')

# Valideren en parse XML-bestand
xml_data = ET.parse('data.xml').getroot()

if xsd.is_valid(xml_data):
    print("XML klopt vergeleken schema.")
    person_data = xsd.to_dict(xml_data)
    
    if 'name' in person_data and 'age' in person_data:
        name = person_data['name']
        age = person_data['age']
        print("Name:", name)
        print("Age:", age)
    else:
        print("'Name' of 'Age' mist bij data.")
else:
    print("XML klopt niet vergeleken schema.")


# ---------------------------------------- test want dict deed het eerst niet (nu wel)
# person_data = xsd.to_dict(xml_data)
# print(person_data) 
# ----------------------------------------