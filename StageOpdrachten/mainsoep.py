from xmlschema import XMLSchema
from xml.etree import ElementTree as ET

# Laden XSD-schema
xsd = XMLSchema('soep.xsd')

# Valideren en parse XML-bestand
xml_data = ET.parse('datasoep.xml').getroot()

# print(ET.tostring(xml_data, encoding='utf-8').decode('utf-8'))

# Valideren
if xsd.is_valid(xml_data):
    print("XML is valid according to the schema.")

    # Overig code
    
    person_data = xsd.to_dict(xml_data)
    
    soepen = ["groentesoep", "tomatensoep", "kippensoep", "champignonsoep", "erwtensoep"]
    
    soep_naam = input("Geef de naam van de soep: ")
    
    if soep_naam in soepen:
        for soep_info in person_data['soepen']['soep']:
            if soep_info['soort'] == soep_naam:
                print("Soort:", soep_info['soort'])
                print("Temperatuur:", soep_info['temperatuur'])
                print("Is vegetarisch:", soep_info['isvegatarisch'])
                print("Ingredient:", soep_info['ingredient'])
                print("Bestek:", soep_info['bestek'])
                break
    else:
        print("Soepnaam niet herkend.")
else:
    print("XML is not valid according to the schema.")
