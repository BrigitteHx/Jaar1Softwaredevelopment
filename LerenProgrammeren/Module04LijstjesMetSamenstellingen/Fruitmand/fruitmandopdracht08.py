# fruitmandopdracht08.py

from fruitmand import fruitmand

totaal_gewicht = 0

watermeloen = {                                                  # watermeloen maken
    "name" : "watermeloen",
    "weight" : 150,
    "color" : "green",
    "round" : True}

fruitmand.append(watermeloen)                                    # watermeloen toevoegen

# for i in range(len(fruitmand)):                                # korte versie zie regel 23, fruit = adres/ element vannuit lijst
#   fruit = fruitmand[i]    
#   print(fruit)

#   totaal_gewicht = totaal_gewicht + fruitmand[i]["weight"]     # gewicht + gewicht + gewicht.. enzovoort 
# print(f"{totaal_gewicht} gram")   

for fruit in fruitmand:                                          # blijft gezien als lijst en niet als range
  totaal_gewicht = totaal_gewicht + fruit["weight"]
print(f"{totaal_gewicht} gram")