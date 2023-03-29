#M04.D01.O3 - Deck van speelkaarten

# import random
# from itertools import product

# faces = range(2,11) + ["King","Queen","Jack","Ace"]
# colour = ["Spades", "Hearts", "Clubs", "Diamonds"]
# (print(f"{random.choice(faces)} of {random.choice(colour)}".format(*card) for card in product(faces, colour)))

# waarde = list(range(2,15))
# kaart = ["klaveren", "ruiten", "schoppen", "harten"]

# bovenkant_kaarten = {
#     11: 'Joker',
#     12: 'Koningin',
#     13: 'Koning',
#     14: 'Aas',
#     'Joker': 11,
#     'Koningin': 12,
#     'Koning': 13,
#     'Aas': 14,
# }

# class Card:
#     def __init__(self, waarde, kaart):
#         self.value = waarde
#         self.suit = kaart

# def generate_cards(waarde, kaart):

# ---------------------------------------------------------------------------------

# import random
# RANKS = list(range(2,15))

# face_cards = {
#     11: 'Joker',
#     12: 'Koningin',
#     13: 'Koning',
#     14: 'Aas',
#     'Joker': 11,
#     'Koningin': 12,
#     'Koning': 13,
#     'Aas': 14,
# }

# SUITS = ["klaveren", "ruiten", "schoppen", "harten"]

# class Deck:
#     def __init__(self):
#         self.cards = []
#         self.build()

#     def build(self):
#         for value in RANKS:
#             for suit in SUITS:
#                 self.cards.append((value, suit))
  
#     def shuffle(self):
#         random.shuffle(self.cards)
        

#     def deal(self):
#         if len(self.cards) > 1:
#             return self.cards.pop()

# ---------------------------------------------------------------------------------

import random

nummer = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Boer', 'Koningin', 'Koning', 'Aas']
soort = ["klaveren", "ruiten", "schoppen", "harten"]
speciaal1 = ["Joker"]
speciaal2 = ["Joker"]
kaarten = []

soort.append(speciaal1)
soort.append(speciaal2) # voegt jokers toe aan kaart

for kaart in soort: 
    for num in nummer: 
        kaarten.append((nummer, soort)) # voegt ze samen



# aantal = 1
# for randomkaart in range(1,8):
#     randomkaart2 = random.choice(kaarten)
#     print(f"kaart {num}: {randomkaart} {randomkaart2} ")
#     # (print(f"Kaart {aantal} : {random.choice(nummer)} {random.choice(soort)})"))
#     aantal += 1 

# print(f"\n Gehele deck: {kaarten}")
print (f'\n deck {len(kaarten)} kaarten: ' , kaarten)


# for random_kaart in range(1,8): #voor de zeven random kaarten
#     random_item = random.choice(kaarten) #kiest een random kaart
#     print(f'kaart {random_kaart} : {random_item}') 
#     kaarten.remove(random_item) #verwijdert de kaart van de list

# print (f'\n deck {len(kaarten)} kaarten: ' , kaarten)