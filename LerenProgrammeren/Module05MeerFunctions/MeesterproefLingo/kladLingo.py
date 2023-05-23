#kladLingo

import random

# als letter juis is mag niet herhalen -> VB carve/cocon -> if elif splitten in 2 runs 

# deze function kiest een woord:
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

# deze funtion is de playthrough
def lingo():
    chosenWord = pickWord()
    letters = list(chosenWord)
    
    #de list() maakt een nieuw "list object", de chosenWord is het argument en hij maakt van de letters losse elementen 
    # ^ "hello" wordt "h""e""l""l""o"
    
    guessAttempts = 0

    print("Welkom bij Lingo!\n")
    print("Raad het ENGELSE 5 letterige woord voordat de pogingen op zijn.\n")
    print("Als een geraade letter goed is én op de juiste plek zal er een X staan.\nAls de letter in het woord zit maar niet op de juiste plek zal er een O staan.")
    print("Je kunt tot 5 keer raden. \n")
    print(chosenWord)

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
        # enumerate() wordt gebruikt om de index en het karakter letter op die index in de guess string te checken (uitleg enumerate beneden)
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
      
lingo()


# enumerate:
# De ingebouwde functie enumerate() in Python wordt gebruikt om iteraties over een sequentie 
# (zoals een lijst, een tuple, een string, enz.) te doorlopen en tegelijkertijd zowel de index als het element op die index te verkrijgen. 
# Het retourneert een iterator die tuples produceert met twee elementen: de index en het overeenkomstige element.