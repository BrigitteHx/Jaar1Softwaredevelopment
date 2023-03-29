#game engine poging 3:

# routes = True

# # titles ophalen uit lijst: uit lijst dict.
# def scenarios_import(scenarios : list,title): 
#     for scenario in scenarios:
#         if scenario['title'] == title:
#             return scenario 

# # story ophalen uit lijst:
# def story_import(scenarios : list,scenes):
#     return scenarios[scenes]['story']

# # route kiezen: 
# def options_route(options : list): 
#     antwoord_opties = []
#     for i in options:
#         print(f"Opties: {0} {i}") # print opties 
#         antwoord_opties.append(i[0]) # voegt opties van scene toe aan lijst 
#     while routes:
#         welke_route = input(str("What way would you like to go? \n")).lower()
#         if welke_route in antwoord_opties: # checken of antwoord goed is 
#             for i in options: 
#                 if i[0] == welke_route:
#                     return i

# # winnen of verliezen/ good or bad ending: 
# def endings(options : list):
#     if options == 'Good_end':
#         print('You earned the good ending, you escaped the maze, congrats!')
#         exit()
#     if options == 'Bad_end': 
#         print('You earned the bad ending, you didnt escape from the maze')
#         exit()
#     else:
#         return True

# # game werking:
# def doolhof_game(scenarios : list, title):
#     game_einde = True
#     while game_einde:
#         scene = scenarios_import(scenarios, title)
#         story = story_import(scenarios, story) 
#         print(story)
#         game_einde = endings(scenarios[scene]['options'])
#         if game_einde:
#             title = options_route(scenarios[scene]['options'])
#     print('The end!')
