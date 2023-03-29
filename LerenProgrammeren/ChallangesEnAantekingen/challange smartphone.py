# challange smartphone

naamiphone = input("Wat is de naam van uw iPhone? " )
prijsiphone = int(input("Hoe duur is uw iPhone? "))

naamsamsung = input("Wat is de naam van uw Samsung? " )
prijssamsung = int(input("Hoe duur is uw Samsung? ")) 

naamzenfone = input("Wat is de naam van uw Zenofone? ")
prijszenfone = int(input("Hoe duur is uw Zenofone? "))

verschil = prijsiphone - prijssamsung
verschil1 = prijsiphone - prijszenfone
verschil2 = prijssamsung - prijszenfone

#duurste 
if prijsiphone > prijssamsung and prijsiphone > prijszenfone :
    naamduurste = naamiphone 
elif prijssamsung > prijszenfone and prijssamsung > prijsiphone : 
    naamduurste = naamsamsung
elif prijszenfone > prijsiphone and prijszenfone > prijssamsung :
    naamduurste = naamzenfone 
elif prijsiphone == prijssamsung and prijsiphone > prijszenfone:
    naamgelijkduurste = f"{naamiphone} {naamsamsung}"
elif prijsiphone == prijszenfone and prijsiphone > prijssamsung : 
    naamgelijkduurste = f"{naamiphone} {naamzenfone}"
elif prijssamsung == prijszenfone and prijssamsung > prijsiphone :
    naamgelijkduurste = f"{naamsamsung} {naamzenfone}"
else : 
    naamgelijkduurste = f"{naamiphone} {naamsamsung} {naamzenfone} " 

#goedkoopste 
if prijsiphone < prijssamsung and prijsiphone < prijszenfone :
    naamgoedkoopste = naamiphone 
elif prijssamsung < prijszenfone and prijssamsung < prijsiphone : 
    naamgoedkoopste = naamsamsung
elif prijszenfone < prijsiphone and prijszenfone < prijssamsung :
    naamgoedkoopste = naamzenfone 
elif prijsiphone == prijssamsung and prijsiphone < prijszenfone:
    naamgelijkgoedkoopste = f"{naamiphone} {naamsamsung}"
elif prijsiphone == prijszenfone and prijsiphone < prijssamsung : 
    naamgelijkgoedkoopste = f"{naamiphone} {naamzenfone}"
elif prijssamsung == prijszenfone and prijssamsung < prijsiphone :
    naamgelijkgoedkoopste = f"{naamsamsung} {naamzenfone}"
else : 
    naamgelijkgoedkoopste = f"{naamiphone} {naamsamsung} {naamzenfone} " 

# middelste 
if prijsiphone > prijssamsung and prijsiphone < prijszenfone :
    naammiddel = naamiphone
elif prijsiphone < prijssamsung and prijsiphone > prijszenfone :
    naammiddel = naamiphone
elif prijssamsung > prijsiphone and prijssamsung < prijszenfone :
    naammiddel = naamsamsung
elif prijssamsung < prijsiphone and prijssamsung > prijszenfone :
    naammiddel = naamsamsung
elif prijszenfone > prijsiphone and prijszenfone < prijssamsung :
    naammiddel = naamzenfone
elif prijszenfone < prijsiphone and prijszenfone > prijssamsung :
    naammiddel = naamzenfone

if prijsiphone > prijssamsung and verschil <= 50 and verschil -50 : 
    print((f"De {naamiphone} is het duurts, de telefoon kost: {prijsiphone} Euro "))
    print(f"De {naamsamsung} is het goedkoopst, de telefoon kost: {prijssamsung} Euro ")
    print(f"Het advies is dus de {naamiphone} te kopen. ")
elif prijsiphone == prijssamsung :
    print(f"De smartphones zijn even duur: {prijsiphone} Euro ")
    print("Ons advies is om de iPhone te kopen, deze is kwalitatief beter. ")
elif prijsiphone and prijssamsung > 900 :
    print(f"De door u gekozen smartphones: {naamiphone} en {naamsamsung} zijn beide boven 900 euro.")
    print("Het advies is dus geen telefoon te kopen, ze zijn te duur.")
elif verschil2 >=100 and verschil1 >=100 :
    print(f"De {naamduurste} is het duurst. ")
    print(f"De {naamgelijkgoedkoopste} is het goedkoopst. ")
    print(f"De {naammiddel} zit er tussenin. ")
    print(f"Het advies is dus de {naamgoedkoopste} te kopen. Deze is namelijk het goedkoopste. ")
else :
    print(f"De {naamiphone} is het duurts, de telefoon kost: {prijsiphone} Euro ")
    print(f"De {naamsamsung} is het goedkoopst, de telefoon kost: {prijssamsung} Euro ")
    print(f"Het advies is dus de {naamsamsung} te kopen, deze is {verschil} Euro goedkoper. ")

