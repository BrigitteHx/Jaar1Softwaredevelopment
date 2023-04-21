# ijssalon re-done

def hoeveelBolletjes(): 
    vragenHoeveel = True
    while vragenHoeveel: 
        aantalBolletjesInput = input("Hoeveel bolletjes zou u graag willen? ")
        if not aantalBolletjesInput.isdigit():
            print("Dat ken ik niet.")
        else:
            aantalBolletjes = int(aantalBolletjesInput)
            if aantalBolletjes >= 9:
                print("Zulke grote porties verkopen wij niet.")
            else:
                return aantalBolletjes

def hoorntjeOfBakje(aantalBolletjes):
    keuzeMaken = True
    while keuzeMaken:
        if aantalBolletjes < 4:
            keuzeHoorntjeBakje = input("Wilt u een hoorntje of een bakje? ")
            if keuzeHoorntjeBakje.lower() in ("hoorntje", "bakje"):
                print(f"Oke, u krijgt {aantalBolletjes} bolletjes in een {keuzeHoorntjeBakje}. ")
                keuzeMaken = False
            else:
                print("Dat ken ik niet")
        elif aantalBolletjes >= 4 and aantalBolletjes <= 8:
            keuzeHoorntjeBakje = 'bakje'
            print(f"U heeft {aantalBolletjes} bolletjes dus u krijgt een {keuzeHoorntjeBakje}. ")
            keuzeMaken = False
    return keuzeHoorntjeBakje

def smakenKiezen(aantalBolletjes): 
    keuzeSmaak = True
    smakenLijst = []
    aantal = 0 
    while keuzeSmaak:
        smaak = input( f"Welke smaak wilt u voor bolletje {aantal+1}?\nA) Aardbei, C) Chocolade of V) Vanille? ")
        if smaak.lower() in ("aardbei","chocolade","vanille"):
            aantal += 1
            smakenLijst.append(smaak.lower()) 
        if aantal == aantalBolletjes:
            keuzeSmaak = False
        else:
            print("Dat ken ik niet")
    return smakenLijst

def toppingsKeuze():
    toppingKiezen = True
    while toppingKiezen:
            topping = input("Wat voor topping wilt u: \nA) Geen, B) Slagroom, C) Sprinkels of D) Caramel Saus? ")
            if topping.lower() in ("a","b","c","d"):
                toppingKiezen = False
            else:
                print("Dat ken ik niet")
    return topping.lower()

def berekenToppingsPrijs(topping, aantalBolletjes, keuzeHoorntjeBakje):
    if topping == "a":
        prijsTopping = 0
    elif topping == "b":
        prijsTopping = 0.50
    elif topping == "c":
        prijsTopping = 0.30 * aantalBolletjes
    elif topping == "d":
        if keuzeHoorntjeBakje == "bakje":
            prijsTopping = 0.90
        elif keuzeHoorntjeBakje == "hoorntje":
            prijsTopping = 0.60
    return round(prijsTopping, 2)

def meerBestellen():
    volgendeBestelling = True 
    while volgendeBestelling:
        meerBestellenInput = input("Wilt u nog meer bestellen? ")
        if meerBestellenInput.lower == "ja":
            doorgaan = True
            volgendeBestelling = False
        elif meerBestellenInput.lower == "nee":
            doorgaan = False
            volgendeBestelling = False
        else: 
            print("Dat ken ik niet")
    return doorgaan
 
def functionBonnetje(prijsTopping, smakenLijst, topping):
    totaalPrijsAlles = 0
    bonnetjeAlles = []
    lijstTotaal = []
    space = "                                        "

    totaalAantalProducten = [
             { 'naam' : 'aardbei',    'hoeveel' : 0,   'prijs' : 1.10},
             { 'naam' : 'chocolade',  'hoeveel' : 0,   'prijs' : 1.10}, 
             { 'naam' : 'vanille',    'hoeveel' : 0,   'prijs' : 1.10},
             { 'naam' : 'bakje',      'hoeveel' : 0,   'prijs' : 0.75},
             { 'naam' : 'hoorntje',   'hoeveel' : 0,   'prijs' : 1.25}
             ] 
    
    for product in totaalAantalProducten:
        for smaak in smakenLijst:
            if smaak == product['naam']:
                product['hoeveel'] += 1

        if product['hoeveel'] > 0:
            lijstTotaal.append(product)

# -------------------------------------------------
    
        productEenPrijs = product['prijs']  
        prijsProduct = product['hoeveel'] * productEenPrijs
        totaalPrijsAlles += prijsProduct 

        bonnetjeAlles.append(f"{product['naam']} {product['hoeveel']} voor:{space}{prijsProduct}\n")
    
# -------------------------------------------------

        if prijsTopping > 0:
            bonnetjeAlles.append(f"{topping}voor:{space}{round(prijsTopping), 2}\n")
        
        totaalPrijsAlles += prijsTopping
        bonnetjeAlles.append(f"Totaal:{space}{round(totaalPrijsAlles), 2}\n")
    
    return bonnetjeAlles



def main():
    again = True
    while again:
        aantal_bolletjes = hoeveelBolletjes()
        keuze_hoorntje_bakje = hoorntjeOfBakje(aantal_bolletjes)
        smaken_lijst = smakenKiezen(aantal_bolletjes) 
        topping = toppingsKeuze()
        prijs_topping = berekenToppingsPrijs(topping, aantal_bolletjes, keuze_hoorntje_bakje)
        bonnetjeAlles = functionBonnetje(prijs_topping, smaken_lijst, topping)
        doorgaan = meerBestellen()
        if doorgaan == False: 
            print(bonnetjeAlles)

# ---------------------------------------------------------------------------------------------------------------------------------------------------------

