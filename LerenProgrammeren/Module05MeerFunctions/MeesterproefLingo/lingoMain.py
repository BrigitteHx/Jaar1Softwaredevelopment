# lingo

from lingoFunctions import *

def main():
    while True:
        titleScreen()
        playAgain = input("Wil je nog een ronde spelen? (ja/nee): ").lower()
        if playAgain.lower() != "ja":
            break

main()