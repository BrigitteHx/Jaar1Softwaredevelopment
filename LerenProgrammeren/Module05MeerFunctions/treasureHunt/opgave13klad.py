# opgave 13 

from data import *
from functions import *


def getEarnigs(profitGold:float, mainCharacter:dict, friends:list, investors:list) -> list:
    people = [mainCharacter] + friends + investors
    earnings = []

    # haal de juiste inhoud op
    adventuringFriends = getAdventuringFriends(friends)
    interestingInvestors = getInterestingInvestors(investors)
    adventuringInvestors = getAdventuringInvestors(investors)
    # investorsCuts = getInvestorsCuts(profitGold ,getInterestingInvestors(investors))
    # goldCut = round(getAdventurerCut(profitGold,investorsCuts,len([mainCharacter]+adventuringFriends+getAdventuringInvestors(investors))),2)

    people = [mainCharacter] + friends + investors 
    peopleTotal = [mainCharacter] + adventuringFriends + adventuringInvestors
    # donateGold = 10
    donateGold = len(adventuringFriends) * 10
    adventuresCut = (profitGold - (getInvestorsCuts(profitGold,investors)) ) / len(peopleTotal)
    gold = 0
  

    # verdeel de uitkomsten
    for person in range(len(people)):
        #code aanvullen

        startAdventure = round(getPersonCashInGold(people[person]['cash']),2)
        endAdventure = startAdventure

        # main character
        if people[person] in [mainCharacter]:
            endAdventure += donateGold + adventuresCut
        # investors 
        elif people[person] in [investors]:
            # investors die mee gingen
            if people[person] in interestingInvestors and people[person] in adventuringInvestors:
                gold = round(profitGold / 100 * people[person][ 'profitReturn'],2)
                endAdventure += gold + adventuresCut
            # investors die niet mee gingen
            elif people[person] in interestingInvestors: # deze mist bij andere methode
                gold = round(profitGold / 100 * people[person][ 'profitReturn'],2)
                endAdventure += gold
        # friends die meegingen
        elif people[person] in [friends]:
            if people[person] in adventuringFriends:
                endAdventure += adventuresCut - 10
        
        earnings.append({
                'name'   : people[person]['name'],
                'start'  : round(startAdventure),
                'end'    : round(endAdventure)
            })      

# VERSION 2 (WERKT NIET)

# def getEarnigs(profitGold:float, mainCharacter:dict, friends:list, investors:list) -> list:
#     people = [mainCharacter] + friends + investors
#     earnings = []

#     # haal de juiste inhoud op
#     adventuringFriends = getAdventuringFriends(friends)
#     interestingInvestors = getInterestingInvestors(investors)
#     adventuringInvestors = getAdventuringInvestors(investors)
#     # investorsCuts = getInvestorsCuts(profitGold ,getInterestingInvestors(investors))
#     # goldCut = round(getAdventurerCut(profitGold,investorsCuts,len([mainCharacter]+adventuringFriends+getAdventuringInvestors(investors))),2)

#     people = [mainCharacter] + friends + investors 
#     peopleTotal = [mainCharacter] + adventuringFriends + adventuringInvestors
#     # donateGold = 10
#     donateGold = len(adventuringFriends) * 10
#     adventuresCut = (profitGold - sum(getInvestorsCuts(profitGold,investors)) ) / len(peopleTotal)
#     gold = 0

#     # verdeel de uitkomsten
#     for person in range(len(people)):
#         #code aanvullen

#         startAdventure = round(getPersonCashInGold(people[person]['cash']),2)
#         endAdventure = startAdventure

#         # main character
#         if people[person] in [mainCharacter]:
#             endAdventure += donateGold + adventuresCut
#         # investors 
#         elif people[person] in [investors]:
#             # investors die mee gingen
#             if people[person] in interestingInvestors and people[person] in adventuringInvestors:
#                 gold = round(profitGold / 100 * people[person][ 'profitReturn'],2)
#                 endAdventure += gold + adventuresCut
#             # investors die niet mee gingen
#             elif people[person] in interestingInvestors: # deze mist bij andere methode
#                 gold = round(profitGold / 100 * people[person][ 'profitReturn'],2)
#                 endAdventure += gold
#         # friends die meegingen
#         elif people[person] in [friends]:
#             if people[person] in adventuringFriends:
#                 endAdventure += adventuresCut - 10
        
#         earnings.append({
#                 'name'   : people[person]['name'],
#                 'start'  : round(startAdventure),
#                 'end'    : round(endAdventure)
#             })  
#     return earnings