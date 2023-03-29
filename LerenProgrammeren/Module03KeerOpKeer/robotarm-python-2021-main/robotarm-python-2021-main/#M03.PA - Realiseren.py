#M03.PA - Realiseren

import random
import time

print("Welcome to the guessing game, this is your first round.\n " )
time.sleep(1)
print("There are 20 rounds, each round you have 10 guesses to guess the mystery number.\n ")
time.sleep(1)
print("If you guess the number on time, you earn a point, with 20 points  you win the game!\n ")
time.sleep(1)

rounds = 0
guesses = 0 
score = 0 

maxrounds = 5
maxguesses = 10
 

while rounds <= maxrounds:
   number = random.randint(1, 1000)
   print(number)
   print(f"Ronde nummer {rounds}")
   guesses = 0 # voor ronde
   while True: # while van maken anders gaat hij 10 keer raden ook als je het al hebt

      guess = int(input("Which number do you think it is? \n ")) 
      difference = abs(number - guess) # absoluut verschil zonder - of + 
   
   
      if guess > number: 
         print("Lower! \n")
      if guess < number:
         print("Higher! \n")
      if guess == number: # onderaan 
         print("You've guesses it! \n") # break toevoegen onder score ivm while true 
         score = score + 1
      guesses = guesses + 1 # na guesses optellen (korter)
      rounds = rounds + 1 

      if guess == number or guesses == maxguesses:
         print("New round!")
         print(f"You have {score} points right now!\n ")
         break
      elif difference < 20:
         print("You're extremely close! \n")
      elif difference < 50:  # elif = anders dan kleiner dan 20 
         print("You're very close to the number! \n")
      # na ronde

   if rounds == maxrounds: # uit while dus niet nodig 
         if score == 5:
            print(f"Congrats, you won with {score} points!")
         else:
            print(f"Game over! You have {score} points!")
         break  
       
       
     


# vaste waardes weghalen, geen break en conditie 