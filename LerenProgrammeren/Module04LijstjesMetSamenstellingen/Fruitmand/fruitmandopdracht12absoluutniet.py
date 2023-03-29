# fruitmandopdracht12absoluutniet

from fruitmand import fruitmand
from operator import itemgetter

# Print de kleur, het gewicht en naam zoals onderstaand voorbeeld
# (dus volledig Nederlands) van het fruit met de langste naam, je mag alleen de code het juiste stuk fruit laten kiezen.

# -------------------------------------------------- internet: 
# def get_longest_name(a_list):
#     count = 0
#     for i in a_list:
#         if len(i) > count: 
#            count = len(i)
#            word = i
#     return word
# def main():
#     print("1.", get_longest_name(["Candide", "Jessie", "Kath", "Amity", 
#    "Raeanne"]))

# from itertools import imap
# max(imap(len, d))

# max(d, key=lambda x: len(x.split()))
   
# -------------------------------------------------- hulp vragen: 
                                                                                                       
def fruit_longest_word(fruitmand):
    return max(fruitmand, key=lambda fruit:len(fruit['name']))

# uitgelegd functie max: 
def fruit_longest_word2(fruitmand):
    fruitmax = fruitmand[0]
    for i in range(1, len(fruitmand)):
        fruit = fruitmand[i]
        if len(fruit['name'])>len(fruitmax['name']):
            fruitmax = fruit
    return fruitmax

# def langste_naam(fruitmand):
#     return max(fruitmand, key=lambda name:len(name['name']))

#aggregraat function !! 1 gegeven onthouden 
# -------------------------------------------------- mislukt:

# totalelengte = 0

# for i in range (0, len(fruitmand)):
#     naamlengte = len(fruitmand[i].get('name'))
#     if naamlengte > totalelengte:
#         naamlengte = totalelengte

# for fruit in range (0, len(fruitmand)):
#     if totalelengte == len(fruitmand[i]['name']):
#         naam = fruitmand[fruit]['name']
#         kleur = fruitmand[fruit]['color']
#         gewicht = fruitmand[fruit]['weight']

# # vertalingen: 

# if kleur == "yellow":
#     kleur = "geel"
# elif kleur == "green":
#     kleur = "groen"
# elif kleur == "red":
#     kleur = "rood"
# elif kleur == "brown":
#     kleur = "bruin"
# elif kleur == "black":
#     kleur = "zwart"
# elif kleur == "purple":
#     kleur = "paars"
# elif kleur == "pink":
#     kleur = "roze"

# print(f'De "{naam}" ({totalelengte} letters) heeft een {kleur} kleur en een gewicht van {gewicht} gram.')