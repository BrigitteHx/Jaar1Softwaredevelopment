# lingo

from lingoFunctions import *

def main():
    while True:
        title_screen()
        playAgain = input("Wil je nog een ronde spelen? (ja/nee): ")
        if playAgain.lower() != "ja":
            break


main()