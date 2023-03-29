# kaas

vraag1 = input("Is de kaas geel? (Ja/Nee)")
if vraag1 == "Nee":
    vraag2 = input("Heeft de kaas blauwe schimmel? (Ja/Nee)")
    if vraag2 == "Nee": 
        vraag3 = input("Heeft de kaas een korst? (Ja/Nee)")
        if vraag3 == "Nee" : 
            print("Mozzarella")
        else : print("Camembert")
    else : 
        vraag4 = input ("Heeft de Kaas een korst ?(Ja/Nee)")
        if vraag4 == "Ja" : 
            print("Blue de Rochbaron")
        else : 
            print("Foume dÁmbert")
if vraag1 == "Ja" :
    vraag5 = input("Zitten er gaten in? (Ja/Nee)")
    if vraag5 == "Ja" :
        vraag6 = input("Is de kaas belachelijk duur? (Ja/Nee)") 
        if vraag6 == "Ja " :
            print("Emmenthaler")
        else :
            print("Leerdammer")
    else :
        vraag7 = input("Is de kaas hard als steen? (Ja/Nee)")
        if vraag7 == "Ja" :
            print("Parmigiano Reggiano")
        else : 
            print("Goudse Kaas")

         