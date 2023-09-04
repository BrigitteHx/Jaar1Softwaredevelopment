from lxml import etree

# Laden XSD 
xsd_tree = etree.parse("soep.xsd")

# Entree module voor xpath 
xsd_schema = etree.XMLSchema(xsd_tree)

# Laden XML 
xml_tree = etree.parse("datasoep.xml")

# ---------------------------------------- internet -> Valideren XML met XSD niet werkend gekregen  
# if xsd_schema.validate(xml_tree):
#     print("XML data is valid according to the XSD schema.")
# else:
#     print("XML data is not valid according to the XSD schema.")
#     print(xsd_schema.error_log)
# ----------------------------------------

# Dict voor soep data
soup_data = {}

# Voor elk element/ soort soep haalt informatie hiervan op uit XML met xpath en slaat deze op in dict
for soup_elem in xml_tree.xpath("//soep"):
    soort = soup_elem.findtext("soort")
    temperatuur = soup_elem.findtext("temperatuur")
    isvegetarisch = soup_elem.findtext("isvegatarisch")
    ingredient = soup_elem.findtext("ingredient")
    bestek = soup_elem.findtext("bestek")
    
    soup_data[soort] = {
        "temperatuur": temperatuur,
        "isvegatarisch": isvegetarisch,
        "ingredient": ingredient,
        "bestek": bestek
    }

# User input welke soep wordt getoont
user_choice = input("Welke soep zou je graag wilen zien? ")

# Wanneer user input in soep data staat, zal info worden geprint
if user_choice in soup_data:
    print(f"Soup: {user_choice}")
    print(f"Temperature: {soup_data[user_choice]['temperatuur']} C")
    print(f"Vegetarian: {'Yes' if soup_data[user_choice]['isvegatarisch'] == 'true' else 'No'}")
    print(f"Ingredient: {soup_data[user_choice]['ingredient']}")
    print(f"Bestek: {soup_data[user_choice]['bestek']}")

# Wanneer user input NIET in soep data staat, print fout
else:
    print("Soep niet gevonden")