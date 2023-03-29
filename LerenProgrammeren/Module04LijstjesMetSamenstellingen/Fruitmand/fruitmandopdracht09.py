# fruitmandopdracht09.py

from fruitmand import fruitmand

for index in range(len(fruitmand)):
    if fruitmand[index]['name'] == 'druif':
        fruitmand.pop(index)
        break

kleuren = []

for fruit in fruitmand:
    if (fruit['color']) not in kleuren:
        kleuren.append(fruit['color'])
print(kleuren)  


# index bij terugvinden 