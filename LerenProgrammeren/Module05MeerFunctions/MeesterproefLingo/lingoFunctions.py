# lingoFunctions

# COLORS ------------------------------------------------------------------------------------------------------------

# ANSI kleuren
class colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    RESET = '\033[0m'


# IMPORT -----------------------------------------------------------------------------------------------------------

from kladLingo import *
import random

# TITLE SCREEN WORKING ---------------------------------------------------------------------------------------------

def title_screen_options():
    option = input("> ")
    if option.lower() == "play":
        lingo()
    elif option.lower() == "quit":
        exit()
    elif option.lower() == "help":
        help_menu()
    else:
        print("Invalid answer, please try again.")
        title_screen_options()


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
    print("Raad het ENGELSE 5-letterige woord voordat de pogingen op zijn.\n")
    print("Als een geraden letter goed is én op de juiste plek zal er een X staan.\nAls de letter in het woord zit maar niet op de juiste plek zal er een O staan.\n")
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
        'clash', 'clean', 'clear', 'clerk', 'click', 'cliff', 'climb', 'clock', 'close', 'cloth'
    ]

    return random.choice(wordList)


# LINGO ----------------------------------------------------------------------------------------------------

def lingo():
    chosenWord = pickWord()
    letters = list(chosenWord)
    X = (colors.RED + "X" + colors.RESET)
    O = (colors.YELLOW + "O" + colors.RESET)

    guessAttempts = 0

    while guessAttempts < 5:
        # print(chosenWord)
        guess = input("Voer je woord in: ").lower()

        if len(guess) != 5:
            print("Niet goed, je woord moet 5 letters lang zijn. Probeer opnieuw.")
            continue

        if guess == chosenWord:
            print("Gefeliciteerd, dat is juist!")
            break

        guessAttempts += 1
        resultGuess = ""
        checkedLetters = []

        # controleer "X"
        for i, letter in enumerate(guess):
            if letter == letters[i]:
                resultGuess += X
                checkedLetters.append(letter)
            else:
                resultGuess += "_"

        # controleer "O"
        for i, letter in enumerate(guess):
            if letter in checkedLetters:
                continue  # skip letters die al "X" zijn
            elif letter in letters:
                resultGuess = resultGuess[:i] + O + resultGuess[i + 1:]

        print("Feedback:", resultGuess)
        print("Raad pogingen over:", 5 - guessAttempts, "\n")

    if guessAttempts >= 5:
        print("Sorry, je hebt geen pogingen meer over.")
        print("Het woord was:", chosenWord)

