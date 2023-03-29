# kladblok


# rounds = 1 
# guesses = 0 
# score2 = 0
# while guesses == 0:
#     print("Starting next round...")
#     guesses = guesses + 1
#     break 

# while rounds > 0 and rounds < 10:
#  nummer = random.randint(1, 1000)
#  print(nummer)
#  poging = int(input("Welk nummer denkt u dat het is? ")) 
#  verschil = poging - nummer 

#  if poging == nummer: 
#     print("Geraden!")
#     rounds = rounds + 1
#     score2 = score2 + 1
#     print("Nieuw nummer laden ... ")
#  elif poging > nummer:
#     print("Lager!")
#     guesses = guesses + 1
#  elif poging < nummer: 
#     print("Hoger")
   #  guesses = guesses + 1

#  elif verschil < 20 or verschil < -20 :
#     print("Je heel erg bent heet!")
#  elif verschil > 20 and verschil < 50 or verschil > -20 and verschil < -50:
#     print("Je bent heet!")
 
#  if guesses == 10:
#     print("Next round!")
#     print(f"Uw score is momenteel {score2}.")
#     guesses = 0
#     rounds = rounds + 1
    
# if rounds == 10:
#     print("Game ended!")
#     print(f"Uw score is {score2}.")
#     print("Loading new round...")
#     rounds = 1