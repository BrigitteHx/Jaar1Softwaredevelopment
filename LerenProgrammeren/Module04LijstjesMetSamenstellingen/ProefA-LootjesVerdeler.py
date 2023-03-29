#Proef A - Lootjes verdeler

import random
namen_lijst = []
lootjes_eind = {}
# aantal_namen = 0
programma = True

print("Welkom tot de loostjes verdeler.")

while programma:
    keuze_naam = input("Wilt u een naam toevoegen?").lower()
    if keuze_naam == "ja":
        naam_invoer = input("Voer een unieke naam in: ")
        if naam_invoer not in namen_lijst:
            namen_lijst.append(naam_invoer)
    elif keuze_naam == "nee" and len(namen_lijst) < 3:
        print("Niet genoeg namen, u moet 3 of meer deelnemers hebben. ")
    else:
        programma = False
        
lootjes_verdelen = True 

while lootjes_verdelen:
    namen_door_elkaar = random.sample(namen_lijst, len(namen_lijst))
    lootjes_verdelen = False
    for i in range(len(namen_lijst)):
        if namen_door_elkaar[i] == namen_lijst[i]:   # vragen index ivm andere naam geeft erorr -> adress en namen doornemen 
            lootjes_verdelen = True                  # checken of namen niet hetzelfde zijn en andersop nieuw

for naam in range(len(namen_lijst)):                 # hier werkt "naam" ipv index wel
    lootjes_eind.update({namen_lijst[naam] : namen_door_elkaar[naam]}) # lijst aan nieuwe directory om te printen

print(lootjes_eind)

#korte namen en specifieker 

# sample() is an inbuilt function of random module in Python that returns a particular length list of items chosen from the sequence i.e. list, tuple, string or set. Used for random sampling without replacement.