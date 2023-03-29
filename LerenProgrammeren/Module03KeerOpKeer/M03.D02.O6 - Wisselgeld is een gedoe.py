#M03.D02.O6 - Wisselgeld is een gedoe 

# name of student: Brigitte Heijkoop
# number of student: 
# purpose of program: Betaal/ wissel methode voor aan bv een kassa
# function of program: Juiste hoeveelheid wisselgeld uitrekenen
# structure of program: zie hieronder

toPay = int(float(input('Amount to pay: '))* 100) 
paid = int(float(input('Paid amount: ')) * 100)
change = paid - toPay
toprint = ""

if change > 0: 
  coinValue = 500 
  
  while change > 0 and coinValue > 0: 
    nrCoins = change // coinValue 

    if nrCoins > 0: 
      print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) 
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) #
      change -= nrCoinsReturned * coinValue 
      totaalreturned = nrCoinsReturned
      totaalvalue = coinValue
      toprint += f"coins returned: {totaalreturned} van {totaalvalue} cents\n" # hetzelfde als toprint = toprint + ..

# comment on code below: Deze code is om de juiste hoeveelheid wisselgeld terug te geven, het rekent uit hoeveel er nog over is en stuur je hiermee door naar de juiste hoeveelheid
    if coinValue == 500:
      coinValue = 300
    elif coinValue == 300:
      coinValue = 200
    elif coinValue == 200:
      coinValue = 100
    elif coinValue == 100:
      coinValue = 50
    elif coinValue == 50:
      coinValue = 20
    elif coinValue == 20:
      coinValue = 10
    elif coinValue == 10:
      coinValue = 5
    elif coinValue == 5:
      coinValue = 2
    elif coinValue == 2:
      coinValue = 1
    else:
      coinValue = 0

if change > 0: # wanneer het nummer niet in bovenstaande lijst staat/ te klein is
  print('Change not returned: ', str(change) + ' cents')
else:
  print(toprint)

