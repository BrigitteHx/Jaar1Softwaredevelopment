#M04.D01.O5 - Boodschappenlijstje


# -----------------------------------------------------------------------------------

# vraag = str(input("Wilt u iets aan uw boodschappenlijst toevoegen? "))
# if vraag == "ja":
#     itemslijst = input("Typ wat u toe wilt voegen hier in, vergeet niet om spaties toe te voegen: ")
#     boodschappenlijst = itemslijst.split(" ")
#     print("\n")
#     print("Uw boodschappen lijst: ")
#     print("\n")
#     for naamitem in boodschappenlijst:
#         print(naamitem)
#     print("\n")
#     print("Nog een fijne dag verder!")
# else: 
#     print("Oke, fijne dag verder. ")

# ----------------------------------------------------------------------------------- 

Lijst = [] 
Aantal = 1
VraagMeer = True # zelfde effect as while true, conditie die hoort bij while

while VraagMeer: 
 ToevoegenAntw = str(input("Wilt u iets aan uw boodschappenlijst toevoegen? "))
 ToevoegenAntw.lower()
 if ToevoegenAntw == "ja": 
    Item = input("Wat wilt u toe voegen aan uw boodschappenlijst? ")
    # if Item == Item:
    #     Aantal =+ 1
    Lijst.append(Item)
 elif ToevoegenAntw == "nee":
    VraagMeer = False

print("Uw boodschappen lijst:")
for x in Lijst: 
    print(Aantal, x)
 
# dictionary voor aantal boodschappen uitzoeken!! 
