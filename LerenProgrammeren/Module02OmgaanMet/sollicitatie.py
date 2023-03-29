#sollicitatie 

print("Welkom bij de sollicitatie Circusdirecteur voor Circus HotelDeBotel, er zullen u een aantal vragen gesteld worden om te zien of u in aanmerking komt.")
print("---------------------------------------------------------------------------------------------------------------------------------------------------")

while True :
    beginvraag = input("Heeft u praktijk ervaring op het gebied van \'Dressuur\', \'Jongleren\' of \'Acrobatiek\'? (Ja/ Nee) ")
    if beginvraag in [ "Ja" , "Nee" ] :
        break

score = 0 

if beginvraag == "Ja" :
    ervaring = input("Waarin heeft U ervaring? ")
    
    if (ervaring == "Dressuur" or "Jongleren" or "Acrobatiek") :
        score = score + 1 
        
    int(input(f'Hoeveel jaar doet u al aan {ervaring}?' ))
    if (ervaring = "Dressuur" > 4) or ( = "Jongleren" >5) or ("Acrobatiek" >3): 
        score = score + 1 



       
            
            
  

# if ((ding1 == 'ervaring1') and (int optie2) or (int optie3)) 