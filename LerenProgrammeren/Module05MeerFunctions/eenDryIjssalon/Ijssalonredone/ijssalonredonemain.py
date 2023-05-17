from ijssalonredone import *

prijsTopping = 0
smakenLijst = []

# ----------------------------------------------------------------------------------------------
    
print("Welkom bij Papi Gelato!\n")

bestellenIjs = True

while bestellenIjs:
    soortKlant = particulierOfZakelijk()
    hoeveelIjs = hoeveelheidBolletjes(soortKlant)
    keuzeHB = hoorntjeBakje(hoeveelIjs, soortKlant)
    smakenLijst.append(keuzeHB)
    smakenLijst += keuzeSmaak(hoeveelIjs, soortKlant)
    toppingKiezen = keuzeTopping(soortKlant)
    prijsTopping += toppingKeuze(toppingKiezen,hoeveelIjs,keuzeHB)

    meerBestellen = bestelling(soortKlant)
    if meerBestellen.lower() in ("nee"):
        print("Bedankt en tot ziens!")
        bestellenIjs = False
 
bonnetje = bonnetje(smakenLijst,prijsTopping,soortKlant)
print("--------------['Papi Gelato']--------------")
for optie in bonnetje:
    print(optie)

# naam function ww_object