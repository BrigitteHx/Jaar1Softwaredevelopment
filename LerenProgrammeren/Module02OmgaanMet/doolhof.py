#doolhof

from time import sleep
score = 0 

print("Welcome to..")
print(" ")
sleep(2)
print("THE MAZE OF MADNESS")
print(" ")
sleep(3)

while True : 
    begin =  input("Are you ready to play? (\'y\'/\'n\') ")
    if begin in [ "y", "Y" ] : 
        print(" ")
        naam = input("There's no turning back now but before you enter the maze, what is your name? ")
        score = 1
        break 
    elif begin in [ "n", "N" ] :
        print("How cowardly, in that case take the walk of shame out of the maze.. ")
        exit()
    else : 
        print("Thats not a correct answer, please try again.")
        
if score == 1 :
    print(" ") 
    print(f"Alright {naam}, you're standing in front of the maze and you can see the 3 ways right in front of you..")
    sleep(1)
    print(" ")
    print("A. What might be laying around that corner? I'm going right!") # keuze 1 
    print("B. I'd like to see more of the Maze, I'm going straight forward. ") # keuze 2
    print("C. But what about left? What will I find there? I'm going to find that out. ") # keuze 3
    print(" ")
    sleep(1) 
    score = 2

while score == 2: 
    choice1 = input("But what way shall you pick? " )
    break
if choice1 == "B" : 
    print(" ")
    print("So you've decided to keep going? ")
    print("Thats great, while you're walking forward you notice something in the distance. ")
    print("Coming closer you realise its an apple tree! ")
    print(" ")
    sleep(1) 
    choice9 = input("Those apples look really good, would you like to take a break and eat some? (y/n) ")
    if choice9 in [ "y", "Y" ] :
        print(" ")
        print("Didnt I mention that you should ever trust a maze?! ")
        print("The apples end up being poisened and you die. ")
        print("Congratulations, you unlocked the BAD ending. ")
        print(" ")
        sleep(1)
        print("Not that you should be proud of it.. Better luck next time! \n") # aantekening 
        exit()
    elif choice9 in [ "n", "N" ] :
        print() # aantekening 
        print("Nice decision to see through that, those apples were poisened! ")
        print("You kept walking and walked straight into victory!")
        print("Good job, you found the exit and unlocked the GOOD ENDING!")
elif choice1 == "A" or choice1 == "C" :
    print(" ")
    print("On the way you come across another intersection..")
    sleep(1)
    print(" ")
    print("A. You choose to ignore the other ways and follow the route, lets go! ") # keuze 4
    print("B. You're going left, what will that way bring you to? ") # keuze 5 
    print("C. That one bush doesn't look so stable, you're not liking this maze very much and decide to climb over it.. ") # keuze 6 
    print(" ")
    sleep(1)
    score = 3
else : 
    print("Thats not a correct answer.. ")

choice4 = ""
while score == 3 : 
    choice4 = input(f"Which way are you going {naam}, what risks are you willing to take? ")
    break
if choice4 == "C" : # einde 3 heg
    print(" ")
    sleep(1)
    print("Oh no! You while you climbed over the bush you hurt yourself, a sprained ankle is never nice.")
    print(f"At least you made it out of the maze quickly, congrats {naam} you earned the SEMI-GOOD ending.")
    exit()
elif choice4 == "A" or choice4 == "B" : # keuze 4 
    print(" ")
    sleep(1)
    print("You've been on your way a little while when you see a bridge in the distance.")
    print("You could also still follow the route.")
    print(" ")
    print(f"So {naam}, your options are: ")
    print("A. Im up for a risk and I'm going for the bridge! ") # keuze 7 
    print("B. Im not so sure about that bridge and I'd rather follow the route. ") # keuze 8 
    score = 4 

choice7 = ""
if score == 4 :
    print(" ")
    sleep(1)
    choice7 = input(f"What option would you like to go with {naam}? ")

if choice7 == "A" : #door brug heen vallen
    print(" ")
    sleep(1)
    print("So you're a though one? Crossing a bridge in a maze, I havent seen a lot people do that before.")
    print("Too bad for you, you shouldn't have done it either...")
    sleep(2)
    print("...")
    sleep(1)
    print("CRACK!")
    print("You fell through the bridge and earned the BAD ENDING.")
    exit()
if choice7 == "B" :
    sleep(1)
    print("Hmm.. that bridge didn't look stable right?")
    print("Nope, I agree, good thing you followed the route though!")
    print("You kept walking and found the exit of the maze. ")
    print("Congrats, you unlocked the GOOD ENDING!")

    # functions!!!