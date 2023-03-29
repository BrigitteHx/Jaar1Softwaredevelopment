# fruitmandopdracht06.py

from fruitmand import fruitmand

# fruit = fruitmand[0]['weight']

for fruit in fruitmand:
    if fruit['name'] == "appel":
        print(fruit['weight'])