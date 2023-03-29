# PizzaCalculator
# Brigitte Heijkoop

smallpizza = 6.99
mediumpizza = 9.99
largepizza = 12.99


while True : 
    keuzepizza = input('Welcome to New-York Pizza, what size of pizza would you like to order? Please pick between \'Small\' \'Medium\' and \'Large\' ' )
    if keuzepizza in [ "Small", "Medium", "Large" ] : 
        break 


if keuzepizza == "Small" :
    hoeveelkleinepizza = int(input("You picked a \'Small\' pizzas how many would you like? "))
    totalkleinepizza = hoeveelkleinepizza * smallpizza 
    print(f'Your total will be {totalkleinepizza} Euros')


elif keuzepizza == "Medium" : 
    hoeveelheidmediumpizza = int(input("You picked a \'Medium\' pizzas how many would you like? "))
    totalmediumpizza = hoeveelheidmediumpizza * mediumpizza 
    print("Your total will be" , totalmediumpizza, "Euros")

elif keuzepizza == "Large" : 
     hoeveelgrotepizza = int(input("You picked a \'Large\' pizzas how many would you like? "))
     totalgrotepizza = hoeveelgrotepizza * largepizza 
     print("Your total will be", totalgrotepizza , "Euros")

print("Your oder has been placed, thank you and New-York Pizza wishes you a nice day.")


