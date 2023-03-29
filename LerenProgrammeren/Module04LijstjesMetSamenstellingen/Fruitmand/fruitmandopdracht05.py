# fruitmandopdracht05.py

from fruitmand import fruitmand

normale_lijst = len(fruitmand) -1                                   # normale volledige lijst, -1 gaat naar laaste naam op de lijst, zie uitleg hieronder
for i in range((normale_lijst), -1, -1):                            # range zorgt voor beginnen aan einde en dan -1 in lijst
    print(fruitmand[i]['name'])

# --------------------------------------------------------          #  oude code

# fruit = fruitmand[0]['name']

# for fruit in fruitmand:
#     print(fruit['name'])

# uitleg:
# len(A)-1 actually is the index of the last element in list A.  
# As in python (and almost all programming languages), array indexes start from 0, so an array with n elements has index of 0, 1, 2, ...,