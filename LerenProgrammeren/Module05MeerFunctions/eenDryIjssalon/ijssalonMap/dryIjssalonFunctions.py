# M05.PA.O2 - Een programma realiseren

# VARIABLES -------------------------------------------------------------------------------------------------------------

MAXBOLLETJES = 9
smaakCount = {'aardbei': 0, 'chocolade': 0, 'vanille': 0}

# FUNCTIONS -------------------------------------------------------------------------------------------------------------

def hoeveelBolletjes():
    while True:
        aantalBolletjesInput = input("Hoeveel bolletjes zou u graag willen? ")
        if not aantalBolletjesInput.isdigit():
            print("Dat ken ik niet.")
        else:
            aantalBolletjes = int(aantalBolletjesInput)
            if aantalBolletjes >= MAXBOLLETJES:
                print("Zulke grote porties verkopen wij niet.")
            else:
                return aantalBolletjes               

def hoorntjeOfBakje(aantalBolletjes):
    if aantalBolletjes > 4:
        keuzeHoorntjeBakje = 'bakje'
        print(f"U heeft {aantalBolletjes} bolletjes dus u krijgt een {keuzeHoorntjeBakje}. ")
    else:
        while True:
            keuzeHoorntjeBakje = input("Wilt u een hoorntje of een bakje? ")
            if keuzeHoorntjeBakje.lower() in ("hoorntje", "bakje"):
                print(f"Oke, u krijgt {aantalBolletjes} bolletjes in een {keuzeHoorntjeBakje}. ")
                return keuzeHoorntjeBakje
            else:
                print("Dat ken ik niet.")

def smakenKiezen(aantalBolletjes):
    smaken = 0
    gekozenSmakenLijst = []
    smakenTellen = {}
    while smaken < aantalBolletjes:  
        gekozenSmaak = input( f"Welke smaak wilt u voor bolletje {smaken+1}?\nA) Aardbei, C) Chocolade of V) Vanille? ")
        if gekozenSmaak.lower() in ("aardbei","chocolade","vanille"):
            smaken += 1
            gekozenSmakenLijst.append(gekozenSmaak.lower()) 
            if gekozenSmaak.lower() not in smakenTellen:
                smakenTellen[gekozenSmaak.lower()] = 1
            else:
                smakenTellen[gekozenSmaak.lower()] += 1
        else:
            print("Dat ken ik niet")
    return gekozenSmakenLijst, smakenTellen

def meerBestellen():
    while True:
        meerBestellenInput = input("Wilt u nog meer bestellen? ")
        if meerBestellenInput.lower() == "ja":
            return True
        elif meerBestellenInput.lower() == "nee":
            print("Bedankt en nog een fijne dag verder!")
            return False
        else:
            print("Dat ken ik niet.")

def functionBonnetje(hoorntjes, bakjes, aantalBolletjes, smakenTellen):
    totalH = hoorntjes * 1.25
    totalBa = bakjes * 0.75
    totalBo = aantalBolletjes * 1.10

    totaalAlles = totalH + totalBa + totalBo
    print("----------[Papi Gelato]----------\n")
    print(f"Hoorntjes:  {hoorntjes} voor {round(totalH, 2)}")
    print(f"Bakjes:     {bakjes} voor {round(totalBa, 2)}")
    print(f"Bolletjes:  {aantalBolletjes} voor {round(totalBo, 2)}")
    print("Kosten per smaak:")
    for smaak, count in smakenTellen():
        smaak_kosten = count * 1.10
        print(f"{smaak}: {count} voor {round(smaak_kosten, 2)}")
    print("--------------------------- +")
    print(f"Totaal:      {round(totaalAlles, 2)}")

def main(smakenTellen):
    doorloopSalon = True
    totaalAantalBolletjes = 0
    totaalHoorntjes = 0
    totaalBakjes = 0

    while doorloopSalon:
        aantalBolletjes = hoeveelBolletjes()
        keuzeHoorntjeBakje = hoorntjeOfBakje(aantalBolletjes)
        smakenKiezen(aantalBolletjes)
        totaalAantalBolletjes += aantalBolletjes
        if keuzeHoorntjeBakje == "hoorntje":
            totaalHoorntjes += 1
        else:
            totaalBakjes += 1

        if not meerBestellen():
            doorloopSalon = False

    functionBonnetje(totaalHoorntjes, totaalBakjes, totaalAantalBolletjes, smakenTellen)

main()