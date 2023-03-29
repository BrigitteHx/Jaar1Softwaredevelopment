# M05.D01.O4 - Namen en leeftijden

def invoer_namen_leeftijden():
    lijst = []
    persoon = {}
    doorgaan = True
    while doorgaan:
        naam = input("welke naam?")
        if naam == "stop":
            doorgaan = False
        else:
            leeftijd = input("hoe oud?")
            persoon = {"naam" : naam, "leeftijd" : leeftijd}
            lijst.append(persoon)
    return lijst

lijst2 = invoer_namen_leeftijden()
print(lijst2)
