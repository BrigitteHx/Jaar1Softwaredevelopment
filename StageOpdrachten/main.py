from xmlschema import XMLSchema
from xml.etree import ElementTree as ET

# Laden XSD-schema
xsd = XMLSchema('example.xsd')

# Valideren en parse XML-bestand + Haalt het hoofd element van XML op en maakt hier een variabele van
xml_data = ET.parse('data.xml').getroot()

# Controle of XML gegevens kloppen volgens XSD schema
if xsd.is_valid(xml_data):
    print("XML klopt vergeleken schema.")

    # Wanneer XML correct, elementen in dictionary in pyhton
    person_data = xsd.to_dict(xml_data)
    
    # Controle juiste elementen in bestand, als correct = print
    if 'name' in person_data and 'age' in person_data:
        name = person_data['name']
        age = person_data['age']
        print("Name:", name)
        print("Age:", age)

    # Een van elementen mist
    else:
        print("'Name' of 'Age' mist bij data.")

# XML gegevens kloppen niet volgens XSD schema
else:
    print("XML klopt niet vergeleken schema.")


# ---------------------------------------- test want dict deed het eerst niet (nu wel)
# person_data = xsd.to_dict(xml_data)
# print(person_data) 
# ----------------------------------------