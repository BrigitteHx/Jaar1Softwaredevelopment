#M04.D01.O3 - Deck van speelkaarten2

import random

nummers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Boer', 'Koningin', 'Koning', 'Aas']
kleuren = ["klaveren", "ruiten", "schoppen", "harten"]
joker1 = "Joker"
joker2 = "Joker"
kaarten = []

kaarten.append(joker1)
kaarten.append(joker2) # voegt jokers toe aan kaart

for kleur in kleuren: 
    for nummer in nummers: 
        kaarten.append({"nummer":nummer, "kleur":kleur}) # voegt ze samen
        
aantal = 1
for randomkaart in range(1,8):
    randomkaart2 = random.choice(kaarten)
    print(f"kaart {aantal}: {randomkaart} {randomkaart2} ")
    kaarten.remove(randomkaart2)
    aantal += 1 

print (f'\n deck {len(kaarten)} kaarten: ' , kaarten)
