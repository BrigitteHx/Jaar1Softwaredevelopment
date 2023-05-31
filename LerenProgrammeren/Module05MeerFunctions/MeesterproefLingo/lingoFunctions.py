# lingoFunctions

# COLORS ------------------------------------------------------------------------------------------------------------

# ANSI escape codes for text colors
class colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    RESET = '\033[0m'

# Example usage
# print(colors.RED + "This is red text!" + colors.RESET)
# print(colors.GREEN + "This is green text!" + colors.RESET)
# print(colors.YELLOW + "This is yellow text!" + colors.RESET)
# print(colors.BLUE + "This is blue text!" + colors.RESET)
# print(colors.MAGENTA + "This is magenta text!" + colors.RESET)
# print(colors.CYAN + "This is cyan text!" + colors.RESET)
# print(colors.WHITE + "This is white text!" + colors.RESET)


# IMPORT -----------------------------------------------------------------------------------------------------------

from kladLingo import * 
import random

# TITLE SCREEN WORKING ---------------------------------------------------------------------------------------------
def title_screen_options():
	option = input("> ")
	if option.lower() == ("play"):
		lingo()
	elif option.lower() == ("quit"):
		exit()
	elif option.lower() == ("help"):
		help_menu()		
	while option.lower() not in ['play', 'help', 'quit']:
		print("Invalid answer, please try again.")
		option = input("> ")
		if option.lower() == ("play"):
			lingo()
		elif option.lower() == ("quit"):
			quit()
		elif option.lower() == ("help"):
			help_menu()

# TITLE SCREEN LOOK ---------------------------------------------------------------------------------------------
def title_screen():
	print(colors.BLUE + "                 WELCOME TO LINGO                  \n" + colors.RESET)
	print(colors.CYAN + "                 > PLAY                  \n" + colors.RESET)
	print(colors.CYAN + "                 > HELP                  \n" + colors.RESET)
	print(colors.CYAN + "                 > QUIT                  \n" + colors.RESET)
	title_screen_options()

# HELP MENU ----------------------------------------------------------------------------------------------------

def help_menu():
	print("\nHELP: \n")
	print("Raad het ENGELSE 5 letterige woord voordat de pogingen op zijn.\n")
	print("Als een gerade letter goed is én op de juiste plek zal er een X staan.\nAls de letter in het woord zit maar niet op de juiste plek zal er een O staan.\n")
	print("Je kunt tot 5 keer raden. \n")
	print("Zorg ervoor dat je in lowercase typt.\n")
	print(colors.BLUE + "                 LINGO                  \n" + colors.RESET)
	print(colors.CYAN + "                 > PLAY                  \n" + colors.RESET)
	print(colors.CYAN + "                 > HELP                  \n" + colors.RESET)
	print(colors.CYAN + "                 > QUIT                  \n" + colors.RESET)
	title_screen_options()

# WORD ----------------------------------------------------------------------------------------------------

def pickWord():
    wordList = [
    'abide', 'about', 'aisle', 'alien', 'alive', 'alloy', 'alpha', 'among', 'angry', 'ankle',
    'apple', 'april', 'argue', 'array', 'asset', 'aunty', 'awake', 'bacon', 'badge', 'basic',
    'batch', 'beach', 'beard', 'beast', 'begin', 'being', 'belle', 'berry', 'bible', 'birth',
    'black', 'blade', 'blank', 'blend', 'bless', 'blind', 'bliss', 'block', 'blood', 'blues',
    'board', 'boast', 'bonus', 'boost', 'bound', 'brave', 'bread', 'break', 'brick', 'bride',
    'brief', 'brisk', 'broad', 'broth', 'brown', 'brush', 'bunch', 'burnt', 'burst', 'bushy',
    'buyer', 'cabin', 'cable', 'cache', 'cagey', 'camel', 'canal', 'candy', 'carve', 'catch',
    'cause', 'cease', 'chain', 'chair', 'chalk', 'charm', 'chase', 'cheek', 'cheer', 'chess',
    'chief', 'child', 'chill', 'china', 'chive', 'cigar', 'civic', 'civil', 'claim', 'clamp',
    'clash', 'clean', 'clear', 'clerk', 'click', 'cliff', 'climb', 'clock', 'close', 'cloth']

    return random.choice(wordList)


# LINGO ----------------------------------------------------------------------------------------------------

def lingo(chosenWord):
    letters = list(chosenWord)
    pickWord()
    
    guessAttempts = 0

    while guessAttempts < 5:
        guess = input("Voer je woord in: ").lower()
    

        if len(guess) != 5:
            print("Niet goed, je woord moet 5 letters lang zijn. Probeer opniew. ")
            continue

        if guess == chosenWord:
            print("Gefeliciteerd, dat is juist! ")
            return

        guessAttempts += 1
        resultGuess = ""
        for i, letter in enumerate(guess):
            if letter == letters[i]:
                resultGuess += "X"
            elif letter in letters:
                resultGuess += "O"
            else:
                resultGuess += "_"

        print("Feedback: ", resultGuess)
        print("Raad pogingen over:", 5 - guessAttempts, "\n")

    print("Sorry, je hebt geen pogingen meer over. ")
    print("Het woord was:", chosenWord) 


title_screen()