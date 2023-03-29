# fruitmandopdracht04.py

from fruitmand import fruitmand
import random 

hoeveelheid = int(input("Voer hier een aantal in: "))
random_fruit = random.randint(0,7)

for i in range (0,hoeveelheid):                                     # range zodat aangegeven hoeveelheid kan printen 
    print(fruitmand[random_fruit]['name'])                          # random fruit als variabele ipv [0] zoals in oude code

# --------------------------------------------------------          oude code

# fruit = fruitmand[0]['name']

# for fruit in fruitmand:
#     print(fruit['name'])
