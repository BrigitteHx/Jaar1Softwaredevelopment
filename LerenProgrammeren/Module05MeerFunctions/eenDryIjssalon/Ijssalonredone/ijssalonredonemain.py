from ijssalonredone import *

prijsTopping = 0
smakenLijst = []

# ----------------------------------------------------------------------------------------------
    
print(begin())

bestellenIjs = True

while bestellenIjs:
    hoeveelBolletjes = hoeveelheidBolletjes()
    keuzeHB = hoorntjeBakje(hoeveelBolletjes)
    smakenLijst.append(keuzeHB)
    smakenLijst += keuzeSmaak(hoeveelBolletjes)
    toppingKiezen = keuzeTopping()
    prijsTopping += toppingKeuze(toppingKiezen,hoeveelBolletjes,keuzeHB)

    meerBestellen = bestelling()
    if meerBestellen.lower() in ("nee"):
        print("Bedankt en tot ziens!")
        bestellenIjs = False
 
bonnetje = bonnetje(smakenLijst,prijsTopping)
print("--------------['Papi Gelato']--------------")
for optie in bonnetje:
    print(optie)