#game_engine_poging4

# nummer geven aan aantal scenarios:
def scenario_nummer(scenarios : list,naam : str) -> int:
    for aantal in range(len(scenarios)):
        if scenarios[aantal]["naam"] == naam:
            return aantal

# route printen en kiezen (hulp van tom):
def route_en_kiezen(options : list) -> str:     # options per vraag in str
    antwoord_input = []                         # lege lijst om antwoord in te stoppen 
    for option in options:
        print(f"{option[0]}. {option}")         # print option nummer en bijbehorende option 
        antwoord_input.append(option[0])        # voegt antwoord toe aan de juiste option
    while True:
        antwoord = input("What way would you like to go?").lower()
        if antwoord in antwoord_input:          # antwoord checken 
            for option in options:
                if option[0] == antwoord:
                    return option               # deze stuurt naar juiste volgende optie 

# goed en slecht einde functie: 
def eindes(options : list):
    if options == "goodend":
        print("Good ending ")
        return False            # stopt 
    elif options == "badend":
        print("Bad ending")
        return False            # stopt
    else:
        return True             # gaat door 

# printen van verhaal 
def story_print(scenarios : list ,scenario : int) -> str:
    return scenarios[scenario]["story"]

# werking van de game:
def game_doolhoof(scenarios : list, naam : str):
    doorloop = True
    while doorloop: 
        scenario = scenario_nummer(scenarios, naam)  
        story = route_en_kiezen(scenarios, scenario)
        print(story)
        doorloop = eindes(scenarios[scenario]['options'])
        if doorloop: 
            naam = route_en_kiezen(scenarios[scenario]['options'])      # geeft gekoze optie nieuwe naam zodat naar volgende
    print("Completed, thank you for playing.")
