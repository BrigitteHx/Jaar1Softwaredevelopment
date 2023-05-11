# ijssalon re-done 

def hoeveelheidBolletjes():
    hoeveelheidVraag = True
    while hoeveelheidVraag:
        try:
            hoeveelBolletjes = int(input("Hoeveel bolletjes wilt u? "))
            if hoeveelBolletjes > 8:
                print("Sorry, zulke grote porties hebben we niet")
            elif 0 < hoeveelBolletjes <= 8:
                hoeveelheidVraag = False
            else: 
                print("Sorry, geen goed aantal!")
        except ValueError:
            print("Sorry, dat ken ik niet!")
    return hoeveelBolletjes

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

def keuzeSmaak(hoeveelBolletjes):
    kiezen  = True
    smakenLijst = []
    teller = 0
    
    while kiezen:
        smaak = input( f"Welke smaak wilt u voor bolletje {teller+1}?\n A) Aardbei, C) Chocolade of V) Vanille? ")
        if smaak.lower() in ("aardbei","chocolade","vanille"):
            teller += 1
            smakenLijst.append(smaak.lower()) 
        else:
            print("Sorry, dat ken ik niet!")
        if teller == hoeveelBolletjes:
            kiezen = False
    return smakenLijst

def hoorntjeBakje(hoeveelBolletjes):
    kiezen = True
    keuzeHB = " "
    
    while kiezen:
        if hoeveelBolletjes <= 3:
            keuzeHB = input(f"Wilt u deze {hoeveelBolletjes} bolletjes in een hoorntje of een bakje? ")
            if  keuzeHB.lower() in ("hoorntje" , "bakje"):
                print(f"Dan krijgt u van mij een {keuzeHB} met {hoeveelBolletjes} bolletjes\n")
                kiezen = False
            else:
                    print("Sorry, dat ken ik niet!")
        elif hoeveelBolletjes >= 4 and hoeveelBolletjes <= 8:
            print(f"Dan krijgt u van mij een bakje met {hoeveelBolletjes} bolletjes\n")
            keuzeHB = "bakje"
            kiezen = False
    return keuzeHB

def keuzeTopping():
    toppingKiezen = True

    while toppingKiezen:
            topping = input("Wat voor topping wilt u: \nA) Geen, B) Slagroom, C) Sprinkels of D) Caramel Saus? ")
            if topping.lower() in ("a","b","c","d"):
                toppingKiezen = False
            else:
                print("Dat ken ik niet, sorry!")
    return topping.lower()

def toppingKeuze(topping, hoeveelBolletjes, keuzeHB):
    if topping == "a":
        prijsTopping = 0
    elif topping == "b":
        prijsTopping = 0.50
    elif topping == "c":
        prijsTopping = 0.30 * hoeveelBolletjes
    elif topping == "d":
        if keuzeHB == "bakje":
            prijsTopping = 0.90
        elif keuzeHB == "hoorntje":
            prijsTopping = 0.60
    return round(prijsTopping,2)

def bestelling(): # loop toevoegen 
    meerBestellen = input("Wilt u nog meer bestellen? ")
    return meerBestellen 


def bonnetje(smakenLijst, prijsTopping):
    totaalPrijs = 0
    bonnetje = []
    lijstVanBon = []

    alleOptiesDict = [
             { 'naam' : 'aardbei', 'hoeveel' : 0, 'prijs' : 0.95},
             { 'naam' : 'chocolade', 'hoeveel' : 0, 'prijs' : 0.95},
             { 'naam' : 'vanille', 'hoeveel' : 0, 'prijs' : 0.95},
             { 'naam' : 'hoorntje', 'hoeveel' : 0, 'prijs' : 1.25 },
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
        uiteindelijkePrijs = optie["hoeveel"] * productPrijs 
        
        totaalPrijs += uiteindelijkePrijs
        bonnetje.append(f'{optie["naam"]} : {productPrijs} x {optie["hoeveel"]} = € {uiteindelijkePrijs}')

    if prijsTopping > 0:
        bonnetje.append(f'topping : € {round(prijsTopping ,2)}')
    
    totaalPrijs += prijsTopping
    bonnetje.append(f"Totaal € {round(totaalPrijs,2):.2f}")
    
    return bonnetje