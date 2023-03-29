# PizzaCalculator2
# Brigitte Heijkoop

smallpizza = 6.99 
mediumpizza = 9.99
largepizza = 12.99


print(f'Welcome to New-York Pizza, what size of pizza would you like to order? The prizer are: Small ({smallpizza}), Medium ({mediumpizza}) or Large ({largepizza}). ')
score = +1 

while score == 1 :
    try: 
        aantal1 = int(input(f'How many small pizzas ({smallpizza}) would you like?'))
        score = 2
    except: 
        print('Please leave a correct answer and try again. ')


while score == 2 :
    try: 
        aantal2 = int(input(f'How many medium pizzas ({mediumpizza}) would you like?'))
        score = +3
    except: 
        print('Please leave a correct answer and try again. ')


while score == 3 :
    try: 
        aantal3 = int(input(f'How many Large pizzas ({largepizza}) would you like?'))
        score = +4
    except: 
        print('Please leave a correct answer and try again. ') 

smallpizzaprize = smallpizza * aantal1
mediumpizzaprize = mediumpizza * aantal2 
largepizzaprize = largepizza * aantal3

totaal = smallpizzaprize + mediumpizzaprize + largepizzaprize

print(f'Your total will be {totaal} euros. ')
