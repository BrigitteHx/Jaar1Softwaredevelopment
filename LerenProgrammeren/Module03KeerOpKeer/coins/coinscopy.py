# Probeer het meegeleverde programma coins.py (coins.zip) helemaal te doorgronden. Er zitten voor jou nog onbekende operators in het programma. Zoek zelf de werking daarvan op.
# Kopieer het programma naar de map nogmaals.
# Breid het uit naar het gebruik van 2, 3 en 5-euro muntstukken.
# Print na de while loop ook een overzicht van alle teruggegeven muntstukken: per soort muntstuk hoeveel zijn er teruggeven.
# Meldt met een print als niet al het vereiste wisselgeld is teruggegeven met munten.
# Voorzie het programma van comments achter alle aangegeven hashes # De comments tonen aan dat je de werking van het programma helemaal hebt begrepen.


# name of student: 
# number of student:
# purpose of program: 
# function of program:
# structure of program: 

toPay = int(float(input('Amount to pay: '))) #
paid = int(float(input('Paid amount: '))) #
change = paid - toPay #

if change > 0: #
  coinValue = 5 #
  
  while change > 0 and coinValue > 0: #
    nrCoins = change // coinValue #

    if nrCoins > 1: #
      print('return maximal ', nrCoins, ' coins of ', coinValue, ' euro' ) #
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' euro did you return? ')) #
      change -= nrCoinsReturned * coinValue #

# comment on code below: 
    if coinValue == 5:
      coinValue = 3
    elif coinValue == 3:
      coinValue = 2
    elif coinValue == 2:
      coinValue = 1
    elif coinValue == 1:
      coinValue = 0.50
    elif coinValue == 0.50:
      coinValue = 0.20
    elif coinValue == 0.20:
      coinValue = 0.10
    elif coinValue == 0.10:
      coinValue = 0.05
    else:
      coinValue = 0

if change > 0: #
  print('Change not returned: ', str(change) + ' cents')
else:
  print('done')