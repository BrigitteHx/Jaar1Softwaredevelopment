# sollicitatie 2 

from re import M


print("Welkom bij de sollicitatie Circusdirecteur voor Circus HotelDeBotel, er zullen u een aantal vragen gesteld worden om te zien of u in aanmerking komt. Op basis van een puntensysteem zult u aan het einde van de vragenlijst niet of u in aanmerking komt. ")
print("---------------------------------------------------------------------------------------------------------------------------------------------------")

nee = "U komt niet in aanmerking voor deze baan"
score = 0

while True :
    beginvraag = input("Heeft u praktijk ervaring op het gebied van \'Dressuur\', \'Jongleren\' of \'Acrobatiek\'? (Ja/ Nee) ")
    if beginvraag in [ "Ja" ] :
        break
    else : 
        raise NameError("Je kunt hier niet werken.")        #error 1
# vragen

name = input("Wat is uw naam?")                             #error 2
if name == "De Jong" and "Slemmer" :
    raise NameError("U bent hier niet welkom!")

age = int(input("Wat is uw leeftijd?"))
if age < 18:
  raise Exception("Je moet ouder dan 18 zijn om hier te kunnen werken.")        #error 3

welke_baan = input("Waar heeft u ervaring in? ")
if welke_baan == "Dressuur" or "Jongleren" or "Acrobatiek" :
  score = score + 1 
else : 
    print("U komt helaas niet in aanmerking voor deze baan.")

hoelang_ervaring = int(input("Hoelang heeft u ervaring? "))
if hoelang_ervaring == "Dressuur" > 4 : 
        score = score + 1
if hoelang_ervaring == "Jongleren" > 5 : 
        score = score + 1
if hoelang_ervaring == "Acrobatiek" > 3 : 
        score = score + 1
        # if waarde = ()
        # waarde is True

mbodiploma = input("Heeft u een MBO diploma? (Ja/Nee) ")
if mbodiploma == "Ja" :
    score = score + 1 

vrachtwagen = input("Heeft u een vrachtwagenbewijs? (Ja/Nee) ")
if vrachtwagen == "Ja" :
    score = score + 1

hogehoed = input("Heeft u een hoge hoed? (Ja/Nee) ")
if hogehoed == "Ja" :
    score = score + 1

manofvrouw = input("Bent u een man of vrouw? (Man/Vrouw) ")
if manofvrouw == "Man" :
    snor = input("Heeft u een van breder dan 10 cm? (Ja/Nee) ")
    if snor == "Ja" : 
        score = score + 1
if manofvrouw == "Vrouw" : 
    haarlengte = input("Heeft u rood krulhaar langer dan 20 cm? (Ja/Nee) ")
    if haarlengte == "Ja" :
        score = score + 1

lengte = input("Bent u langer dan 150 cm? (Ja/Nee)" ) 
if lengte == "Yes" :
    score = score + 1

gewicht = input("Bent u zwaarder dan 90 kilo? (Ja/nee)" )
if gewicht == "Ja" :
    score = score + 1

certificaat = input("Bent u in bezit van het certificaat 'Overleven met gevaarlijk personeel'? (Ja/Nee) ")
if certificaat == "Ja" :
    score = score + 1

if score == 7 : 
    print("U bent geschikt voor deze baan, stuur ons snel je CV!")
elif score > 7 : 
    print("U bent geschikt voor deze baan, stuur ons snel je CV!")
else:
    score < 7
    print("U komt helaas niet in aanmerking voor deze baan.")

exit()


 