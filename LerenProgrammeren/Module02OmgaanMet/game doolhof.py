# game doolhof 
from time import sleep 
score = 0 

begin = input("Welcome to the Maze of Madness, are you ready to play? (y/n) ")

if begin == "y" :
    naam = input("There's no turning back now but before you enter the maze, what is your name? ")
    score = 1
elif begin == "n" : 
    print("How cowardly, in that case take the walk of shame out of the maze.. ")
    exit()

if score == 1 :
    print(" ")
    print(f"Alright {naam}, you're standing in front of the maze and you can see the 3 ways right in front of you..")
    sleep(1)
    print(" ")
    print("A. What might be laying around that corner? I'm going right!") # keuze 1 
    print("B. I'd like to see more of the Maze, I'm going straight forward. ") # keuze 2
    print("C. But what about left? What will I find there? I'm going to find that out. ") # keuze 3 
score = 2

if score == 2 :
    print(" ")
    sleep(1)
    choice1 = input("But what way shall you pick? " )
else : 
    print('Please leave a correct answer and try again. ')

if choice1 == "B" : 
    print(" ")
    print("So you've decided to keep going? ")
    print("Thats great, while you're walking forward you notice something in the distance. ")
    print("Coming closer you realise its an apple tree! ")
    sleep(1) 
    choice9 = input("Those apples look really good, would you like to take a break and eat some? (y/n) ")
    # if choice9 == "y" :

if choice1 == "A" or "C" :
    print(" ")
    print("On the way you come across another intersection..")
    sleep(1)
    print(" ")
    print("A. You choose to ignore the other ways and follow the route, lets go! ") # keuze 4
    print("B. You're going left, what will that way bring you to? ") # keuze 5 
    print("C. That one bush doesn't look so stable, you're not liking this maze very much and decide to climb over it.. ") # keuze 6 
    score = 3

if score == 3 :
    print(" ")
    sleep(1)
    choice4 = input(f"Which way are you going {naam}, what risks are you willing to take? ")
else : 
    print('Please leave a correct answer and try again. ')

 
if choice4 == "C" : # einde 3 heg
    print(" ")
    sleep(1)
    print("Oh no! You while you climbed over the bush you hurt yourself, a sprained ankle is never nice.")
    print(f"At least you made it out of the maze quickly, congrats {naam} you earned the *semi-good* ending.")
    exit()

elif choice4 == "A" or "B" : # keuze 4 
    print(" ")
    sleep(1)
    print("You've been on your way a little while when you a bridge in the distance.")
    print("You could also still follow the route.")
    print(" ")
    print(f"So {naam}, your options are: ")
    print("A. Im up for a risk and I'm going for the bridge! ") # keuze 7 
    print("B. Im not so sure about that bridge and I'd rather follow the route. ") # keuze 8 
    print(" ")
score = 4 

if score == 4 :
    print(" ")
    sleep(1)
    choice7 = input(f"What option would you like to go with {naam}? ")
else :
        print('Please leave a correct answer and try again. ')

if choice7 == "A" : #door brug heen vallen
    print(" ")
    sleep(1)
    print("So you're a though one? Crossing a bridge in a maze, I havent seen a lot people do that before.")
    print("Too bad for you, you shouldn't have done it either...")
    print("CRACK!")
    print("You fell through the bridge and earned the *bad ending*.")

elif choice7 == "B" : # goed einde
    print("Very, very wise descision to follow the route, that bridge wasnt stable at all.")
    print("You kept going straight to the exit and found the exit!")
    print(f"Congrats, you unlocked the *good ending*! Have a wonderful rest of your day {naam}.")

