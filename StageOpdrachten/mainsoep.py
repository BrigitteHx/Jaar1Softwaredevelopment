# from xmlschema import XMLSchema
# from xml.etree import ElementTree as ET

# # Laden XSD-schema
# xsd = XMLSchema('soep.xsd')

# # Valideren en parse XML-bestand
# xml_data = ET.parse('datasoep.xml').getroot()

# # print(ET.tostring(xml_data, encoding='utf-8').decode('utf-8'))

# # Valideren
# if xsd.is_valid(xml_data):
#     print("XML is valid according to the schema.")
    
#     person_data = xsd.to_dict(xml_data)
    
#     soepen = ["groentesoep", "tomatensoep", "kippensoep", "champignonsoep", "erwtensoep"]
    
#     soep_naam = input("Geef de naam van de soep: ")
    
#     if soep_naam in soepen:
#         for soep_info in person_data['soepen']['soep']:
#             if soep_info['soort'] == soep_naam:
#                 print("Soort:", soep_info['soort'])
#                 print("Temperatuur:", soep_info['temperatuur'])
#                 print("Is vegetarisch:", soep_info['isvegatarisch'])
#                 print("Ingredient:", soep_info['ingredient'])
#                 print("Bestek:", soep_info['bestek'])
#                 break
#     else:
#         print("Soepnaam niet herkend.")
# else:
#     print("XML is not valid according to the schema.")

#  ----------------------------------------------------------------------------------------------------------------------------------------------------------

from lxml import etree

# Laden XSD 
xsd_tree = etree.parse("soep.xsd")
xsd_schema = etree.XMLSchema(xsd_tree)

# Laden XML 
xml_tree = etree.parse("datasoep.xml")

# ---------------------------------------- internet -> Valideren XML met XSD 
# if xsd_schema.validate(xml_tree):
#     print("XML data is valid according to the XSD schema.")
# else:
#     print("XML data is not valid according to the XSD schema.")
#     print(xsd_schema.error_log)
# ----------------------------------------

# Dict voor soep data
soup_data = {}
for soup_elem in xml_tree.xpath("//soep"):
    soort = soup_elem.findtext("soort")
    temperatuur = soup_elem.findtext("temperatuur")
    is_vegetarian = soup_elem.findtext("isvegatarisch")
    ingredient = soup_elem.findtext("ingredient")
    bestek = soup_elem.findtext("bestek")
    
    soup_data[soort] = {
        "temperatuur": temperatuur,
        "is_vegetarian": is_vegetarian,
        "ingredient": ingredient,
        "bestek": bestek
    }

user_choice = input("Which soup would you like to see? ")

# Soep printen als user choice goed is 
if user_choice in soup_data:
    print(f"Soup: {user_choice}")
    print(f"Temperature: {soup_data[user_choice]['temperatuur']} C")
    print(f"Vegetarian: {'Yes' if soup_data[user_choice]['is_vegetarian'] == 'true' else 'No'}")
    print(f"Ingredient: {soup_data[user_choice]['ingredient']}")
    print(f"Bestek: {soup_data[user_choice]['bestek']}")
else:
    print("Soep niet gevonden")

