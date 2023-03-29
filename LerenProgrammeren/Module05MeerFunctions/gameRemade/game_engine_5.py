#game_engine_5

from game_info_5 import *
import sys
import time

# SPELER ---------------------------------------------------------------------------------------------
class player:
    def __init__(person):
        person.name = ''
        person.position = 'ground' # begin
        person.won = False
        person.solves = 0
player1 = player()

# TITLE SCREEN WORKING ---------------------------------------------------------------------------------------------
def title_screen_options():
	option = input("> ")
	if option.lower() == ("play"):
		setup_game()
	elif option.lower() == ("quit"):
		exit()
	elif option.lower() == ("help"):
		help_menu()		
	while option.lower() not in ['play', 'help', 'quit']:
		print("Invalid answer, please try again.")
		option = input("> ")
		if option.lower() == ("play"):
			setup_game()
		elif option.lower() == ("quit"):
			sys.exit()
		elif option.lower() == ("help"):
			help_menu()

# TITLE SCREEN LOOK ---------------------------------------------------------------------------------------------
def title_screen():
	print('Welcome to the maze of madness')
	print("                 > Play                  ")
	print("                 > Help                  ")
	print("                 > Quit                  ")
	title_screen_options()

# HELP MENU ---------------------------------------------------------------------------------------------
def help_menu():
	print("")
	print("Use 'move' and 'right' to navigate through the maze.")
	print("")
	print("Use 'examine' and 'look' to load puzzels in differen areas. ")
	print("")
	print("Please ensure to type in lowercase. \n")
	print("    Please select an option to continue.     ")
	print('Welcome to the maze of madness')
	print("                 > Play                  ")
	print("                 > Help                  ")
	print("                 > Quit                  ")
	title_screen_options()

quitgame = 'quit'

# PRINT LOCATION ---------------------------------------------------------------------------------------------
def print_location():
	print(f'LOCATION:{player1.position.upper()}.\n')
	print((maze[player1.position][DESCRIPTION]))

# INPUT GAME ---------------------------------------------------------------------------------------------
def prompt():
	if player1.solves == 5:
		print("Something in the maze seems to have changed. Hmm...")
	print("What would you like to do?")
	action = input("> ")
	acceptable_actions = ['move', 'go', 'travel', 'walk', 'quit', 'inspect', 'examine', 'look', 'search'] # goede antwoorden 
	while action.lower() not in acceptable_actions:
		print("Wrong answer, please try again.\n")
		action = input("> ")
	if action.lower() == quitgame:
		sys.exit()
	elif action.lower() in ['move', 'go', 'travel', 'walk']:
		move(action.lower())
	elif action.lower() in ['inspect', 'examine', 'look', 'search']:
		examine()

# MOVEMENT FUNCTION ---------------------------------------------------------------------------------------------
def move(myAction):
	askString = (f"Where would you like to {myAction} to?\n> ")
	destination = input(askString)
	if destination == 'forward':
		move_dest = maze[player1.position][SIDE_UP] # als je op de grond bent moet het north zeggen
		move_player(move_dest)
	elif destination == 'left':
		move_dest = maze[player1.position][SIDE_LEFT]
		move_player(move_dest)
	elif destination == 'right':
		move_dest = maze[player1.position][SIDE_RIGHT]
		move_player(move_dest)
	elif destination == 'back':
		move_dest = maze[player1.position][SIDE_DOWN]
		move_player(move_dest)
	else:
		print("Wrong answer, try using forward, back, left, or right.\n")
		move(myAction)

# SHOWS WHAT PLAYER DID ---------------------------------------------------------------------------------------------
def move_player(move_dest):
	print(f"\nYou have moved to the {move_dest}.")
	player1.position = move_dest
	print_location()

# LOOK AROUND FUNCTION ---------------------------------------------------------------------------------------------
def examine():
	if room_solved[player1.position] == False:
		print(f'\n{(maze[player1.position][INFO])}')
		print((maze[player1.position][PUZZLE]))
		puzzle_answer = input("> ")
		checkpuzzle(puzzle_answer)
	else:
		print("There is nothing new for you to see here.") # al daar geweest of al gezien

# CHECK PUZZEL ---------------------------------------------------------------------------------------------
def checkpuzzle(puzzle_answer):
	if player1.position == 'ground':
		if player1.solves >= 5:
			endspeech = ("Without you having done anything, the key begins to rotate.\nAll of the mazes walls begin to crumble.\nLight begins to shine over whats remaining from the walls.\nA blinding flash of light hits you and you close your eyes.\nYou have escaped!")
			for character in endspeech:
				sys.stdout.write(character)
				sys.stdout.flush()
				time.sleep(0.05)
			print("\nCONGRATULATIONS!") # einde
			sys.exit()
		else:
			print("Nothing seems to happen still... Look for more puzzles")
	else:
		if puzzle_answer == (maze[player1.position][SOLVED]):
			room_solved[player1.position] = True
			player1.solves += 1
			print("You have solved the puzzle. To the next one!")
			print(f"\nPuzzles solved: {str(player1.solves)}")
		else:
			print("Wrong answer! Try again.\n")
			examine()

# LOOP ---------------------------------------------------------------------------------------------
def main_game_loop():
	while player1.won is False:
		prompt()

# WALK THROUGH ---------------------------------------------------------------------------------------------
def setup_game():

	#naam'
	question1 = "Hello there, who is brave enough to enter the maze of madness?\n"
	for character in question1:
		#type effect
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.05)
	player_name = input("> ")
	player1.name = player_name

	#alle boven samenvoegen
	question3 = (f"Well then, {player1.name}, goodluck. \n ")
	for character in question3:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.05)

	# puzzels in doolhof en start game 
	text1 = (f"It seems this is where we must split {player1.name}.\n")
	text2 = "How unfortunate.\n"  
	text3 = "Oh, you don't know where you are?  Well...\n"
	text4 = "Luckily, I've left you in a little puzzle.  Hopefully you can escape this maze.\n"
	for character in text1:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.05)
	for character in text2:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.1)
	for character in text3:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.05)
	for character in text4:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.05)
	time.sleep(1)

	print("Here begins the adventure... \n")
	print("You find yourself in the center of a strange place.\nSeems like you are in maze.\n")
	print("You see an intersection, with 5 options.\nWhich turn do you take...\n")
	main_game_loop()
title_screen()