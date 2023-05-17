# ijssalon re-done 
sorryError = "Sorry dat is geen optie die we aanbieden..."

def particulierOfZakelijk():
    keuzeKlant = True
    while keuzeKlant:
        soortKlant = input("Bent u 1) een particuliere klant of 2) een zakelijke klant? ")
        if soortKlant.lower() in ("1", "2"):
            keuzeKlant = False
        else:
            print(sorryError)
    return soortKlant

def hoeveelheidBolletjes(soortKlant):
    hoeveelheidVraag = True
    while hoeveelheidVraag:
        try:    
            if soortKlant == "1":
                hoeveelIjs = int(input("Hoeveel bolletjes wilt u? "))
                if hoeveelIjs > 8:
                    print(sorryError)
                elif 0 < hoeveelIjs <= 8:
                    hoeveelheidVraag = False
                else: 
                    print(sorryError)
            elif soortKlant == "2":
                hoeveelIjs = int(input("Hoeveel liter wilt u? "))
        except ValueError:
                print(sorryError)
        return hoeveelIjs

# def hoeveelBolletjes(): 
#     vragenHoeveel = True
#     while vragenHoeveel: 
#         aantalBolletjesInput = input("Hoeveel bolletjes zou u graag willen? ")
#         if not aantalBolletjesInput.isdigit():
#             print("Dat ken ik niet.")
#         else:
#             aantalBolletjes = int(aantalBolletjesInput)
#             if aantalBolletjes >= 9:
#                 print("Zulke grote porties verkopen wij niet.")
#             else:
#                 return aantalBolletjes

def keuzeSmaak(hoeveelIjs, soortKlant):
    kiezen  = True
    smakenLijst = []
    teller = 0

    if soortKlant == "1":
        soort = "bolletjes"
    if soortKlant == "2":
        soort = "liter"
    
    while kiezen:
        smaak = input( f"Welke smaak wilt u voor {soort} {teller+1}?\n A) Aardbei, C) Chocolade, M) Munt of V) Vanille? ")
        if smaak.lower() in ("aardbei","chocolade","vanille", "munt"):
            teller += 1
            smakenLijst.append(smaak.lower()) 
        else:
            print(sorryError)
        if teller == hoeveelIjs:
            kiezen = False
    return smakenLijst

def hoorntjeBakje(hoeveelIjs, soortKlant):
    kiezen = True
    keuzeHB = " "
    
    while kiezen:
        if soortKlant == "1":
            if hoeveelIjs <= 3:
                keuzeHB = input(f"Wilt u deze {hoeveelIjs} bolletjes in een hoorntje of een bakje? ")
                if  keuzeHB.lower() in ("hoorntje" , "bakje"):
                    print(f"Dan krijgt u van mij een {keuzeHB} met {hoeveelIjs} bolletjes\n")
                    kiezen = False
                else:
                        print(sorryError)
            elif hoeveelIjs >= 4 and hoeveelIjs <= 8:
                print(f"Dan krijgt u van mij een bakje met {hoeveelIjs} bolletjes\n")
                keuzeHB = "bakje"
                kiezen = False
        
        elif soortKlant == "2":
            kiezen = False
    return keuzeHB

def keuzeTopping(klantSoort):
    toppingKiezen = True

    while toppingKiezen:
            if klantSoort == "1":
                topping = input("Wat voor topping wilt u: \nA) Geen, B) Slagroom, C) Sprinkels of D) Caramel Saus? ")
                if topping.lower() in ("a","b","c","d"):
                    toppingKiezen = False
                else:
                    print(sorryError)
            elif klantSoort == "2":
                topping = "a"
                toppingKiezen = False
    return topping.lower()

def toppingKeuze(topping, hoeveelIjs, keuzeHB):
    if topping == "a":
        prijsTopping = 0
    elif topping == "b":
        prijsTopping = 0.50
    elif topping == "c":
        prijsTopping = 0.30 * hoeveelIjs
    elif topping == "d":
        if keuzeHB == "bakje":
            prijsTopping = 0.90
        elif keuzeHB == "hoorntje":
            prijsTopping = 0.60
    return round(prijsTopping,2)

def bestelling(klantSoort):
    vragenMeerBestellen = True
    while vragenMeerBestellen:
        if klantSoort == "1":
            meerBestellen = input("Wilt u nog meer bestellen? ")
        elif klantSoort == "2":
            meerBestellen = "nee"

        if meerBestellen in ("ja", "nee"):
            return meerBestellen
        vragenMeerBestellen = False

def bonnetje(smakenLijst, prijsTopping, soortKlant):
    totaalPrijs = 0
    bonnetje = []
    lijstVanBon = []

    alleOptiesDict = [
             { 'naam' : 'aardbei', 'hoeveel' : 0, 'prijs' : 1.10},
             { 'naam' : 'chocolade', 'hoeveel' : 0, 'prijs' : 1.10},
             { 'naam' : 'vanille', 'hoeveel' : 0, 'prijs' : 1.10},
             { 'naam' : 'munt', 'hoeveel' : 0, 'prijs' : 1.10},
             { 'naam' : 'hoorntje', 'hoeveel' : 0, 'prijs' : 1.25},
             { 'naam' : 'bakje', 'hoeveel' : 0, 'prijs' : 0.75}]
    
    
    for optie in alleOptiesDict: # smaken
        for smaak in smakenLijst:
            if smaak == optie['naam']:
                optie['hoeveel'] += 1

    for product in alleOptiesDict: # zorgt ervoor dat alleen boven 0 erop staat 
        print
        if product['hoeveel'] > 0:
            lijstVanBon.append(product) 
    
    # ----------------------------------------------------------------------------------------------
    
    for optie in lijstVanBon:
        productPrijs = optie["prijs"]

        if soortKlant == "2":
            uiteindelijkePrijs = optie["hoeveel"] * 9.80
            productPrijs = 9.80

        elif soortKlant == "1":
           uiteindelijkePrijs = optie["hoeveel"] * productPrijs 
    
        
        totaalPrijs += uiteindelijkePrijs
        bonnetje.append(f'{optie["naam"]} : {productPrijs} x {optie["hoeveel"]} = € {uiteindelijkePrijs}')

    if prijsTopping > 0:
        bonnetje.append(f'topping : € {round(prijsTopping ,2)}')

    if soortKlant == 2:
        bonnetje.append(F"BTW 9%) : € {round((prijsTopping) / 100 * 9) ,2}")
    
    totaalPrijs += prijsTopping
    bonnetje.append(f"Totaal € {round(totaalPrijs,2):.2f}")
    
    return bonnetje