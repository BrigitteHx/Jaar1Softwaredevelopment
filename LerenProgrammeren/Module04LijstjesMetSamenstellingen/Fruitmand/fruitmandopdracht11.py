# fruitmandopdracht11

# checken kleur in lijst
# nieuwe lijst/ dictionary met gekozen kleuren
# nieuwe lijst checken voor meer ronde of meer niet ronde of evenveel (print met if)
# als verschil, reken verschil in hoeveelheid ronde en niet ronde vruchten uit

from fruitmand import fruitmand

lijstkleuren = []

for i in range (len(fruitmand)): # zonder i 
    if fruitmand[i]['color'] is not lijstkleuren: 
        lijstkleuren.append(fruitmand[i]['color'])
        
while True: #condition
    kleurenkiezen = input('Kies uit de volgende kleuren: yellow, brown, green, red and/or orange. ')
    if kleurenkiezen.lower() in lijstkleuren:
        print(f'De kleur {kleurenkiezen} zit in de fruitmand. ')
        break 
    else: 
        print(f'De kleur {kleurenkiezen} zit niet in de fruitmand. ')

# --------------------------------------------------------------------------------------------------------------------------------

aantalronde = 0
aantalnietronde = 0

for x in range(len(fruitmand)): 
    if fruitmand[x]['round'] == True and fruitmand[x]['color'] == kleurenkiezen: 
        aantalronde += 1
    elif fruitmand[x]['round'] == False and fruitmand[x]['color'] == kleurenkiezen: 
        aantalnietronde += 1 

verschilrond = abs(aantalronde - aantalnietronde)

if aantalronde > aantalnietronde:
    print(f'Er zijn {verschilrond} meer ronde vruchten dan niet ronde vruchten in de kleur {kleurenkiezen}')
elif aantalronde < aantalnietronde: 
    print(f"Er zijn {verschilrond} minder ronde vruchten dan niet ronde vruchten in de kleur {kleurenkiezen}")
else: 
    print(f"Er zijn {verschilrond} ronde vruchten en {verschilrond} niet ronde vruchten in de kleur {kleurenkiezen}")
    
