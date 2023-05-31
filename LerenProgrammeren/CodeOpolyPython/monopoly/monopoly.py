# MONOPOLY

# IMPORTS

import random

# PLAYER PROPERTY
class Property:
    def __init__(self, name, price, rent):
        self.name = name
        self.price = price
        self.rent = rent
        self.owner = None 

# BOARD
board = [
    Property("Go", 0, 0),
    Property("Mediterranean Avenue", 60, 2),
    Property("Community Chest", 0, 0),
    Property("Baltic Avenue", 60, 4),
    Property("Income Tax", 0, 0),
    Property("Reading Railroad", 200, 25),
    Property("Oriental Avenue", 100, 6),
    Property("Chance", 0, 0),
    Property("Vermont Avenue", 100, 6),
    Property("Connecticut Avenue", 120, 8),
    Property("Jail", 0, 0),
    Property("St. Charles Place", 140, 10),
    Property("Electric Company", 150, 0),
    Property("States Avenue", 140, 10),
    Property("Virginia Avenue", 160, 12),
    Property("Pennsylvania Railroad", 200, 25),
    Property("St. James Place", 180, 14),
    Property("Community Chest", 0, 0),
    Property("Tennessee Avenue", 180, 14),
    Property("New York Avenue", 200, 16),
    Property("Free Parking", 0, 0),
    Property("Kentucky Avenue", 220, 18),
    Property("Chance", 0, 0),
    Property("Indiana Avenue", 220, 18),
    Property("Illinois Avenue", 240, 20),
    Property("B. & O. Railroad", 200, 25),
    Property("Atlantic Avenue", 260, 22),
    Property("Ventnor Avenue", 260, 22),
    Property("Water Works", 150, 0),
    Property("Marvin Gardens", 280, 24),
    Property("Go To Jail", 0, 0),
    Property("Pacific Avenue", 300, 26),
    Property("North Carolina Avenue", 300, 26),
    Property("Community Chest", 0, 0),
    Property("Pennsylvania Avenue", 320, 28),
    Property("Short Line", 200, 25),
    Property("Chance", 0, 0),
    Property("Park Place", 350, 35),
    Property("Luxury Tax", 0, 0),
    Property("Boardwalk", 400, 50)
]

# PRINT BOARD
for property in board:
    print(f"{property.name} - Price: ${property.price}, Rent: ${property.rent}")


# PLAYER MONEY
class Player:
    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.position = 0  # 0 = place Go in dict

# PLAYERS
player1 = Player("Player 1", 1500)
player2 = Player("Player 2", 1500)

# PRINT INFO 
# print(f"{player1.name} - Money: ${player1.money}, Position: {player1.position}")
# print(f"{player2.name} - Money: ${player2.money}, Position: {player2.position}")

# ROLLING DICE
def roll_dice():
    return random.randint(1, 6)

# PLAYER MOVEMENT
def move_player(player, steps):
    player.position = (player.position + steps) % len(board)

# PASSING GO = + 200 MONEY
def pass_go(player):
    player.money += 200

# TEST ABOVE 
# dice_roll = roll_dice()
# move_player(player1, dice_roll)
# print(f"{player1.name} rolled a {dice_roll} and moved to position {player1.position}")

# pass_go(player1)
# print(f"{player1.name} passed Go and collected $200. Money: ${player1.money}")

# PROPERTY PURCHASE 
def purchase_property(player, property):
    if player.money >= property.price:
        player.money -= property.price
        property.owner = player.name  # !! owner
        print(f"{player.name} purchased {property.name} for ${property.price}. Money: ${player.money}")
    else:
        print(f"{player.name} doesn't have enough money to purchase {property.name}.")

# RENT PAYMENT
def pay_rent(player, property):
    rent = property.rent
    if player.money >= rent:
        player.money -= rent
        print(f"{player.name} paid ${rent} rent to {property.owner}. Money: ${player.money}")
    else:
        print(f"{player.name} doesn't have enough money to pay rent to {property.owner}.")

# TEST
# player1.money = 1000  # player 1 minder money voor test 
# purchase_property(player1, board[1])  # player 1 koopt Mediterranean Avenue
# pay_rent(player1, board[1])  # player 1 betaald rent voor Mediterranean Avenue

# CHECK PLAYER WON
def has_won(player):
    return False

# MAIN LOOP
game_over = False
while not game_over:
    # player 1 
    print(f"\n{player1.name}'s turn:")
    dice_roll = roll_dice()
    move_player(player1, dice_roll)
    print(f"{player1.name} rolled a {dice_roll} and moved to position {player1.position}")

    # check voorbij GO
    if player1.position == 0:
        pass_go(player1)
        print(f"{player1.name} passed Go and collected $200. Money: ${player1.money}")

    # property 
    current_property = board[player1.position]
    if current_property.price > 0:
        if current_property.owner is None:
            purchase_property(player1, current_property)
        elif current_property.owner != player1:
            pay_rent(player1, current_property)

    # check winnen
    if has_won(player1):
        print(f"{player1.name} has won the game!")
        game_over = True

    # player 2
    print(f"\n{player2.name}'s turn:")
    dice_roll = roll_dice()
    move_player(player2, dice_roll)
    print(f"{player2.name} rolled a {dice_roll} and moved to position {player2.position}")

    # check voorbij GO
    if player2.position == 0:
        pass_go(player2)
        print(f"{player2.name} passed Go and collected $200. Money: ${player2.money}")

    # property
    current_property = board[player2.position]
    if current_property.price > 0:
        if current_property.owner is None:
            purchase_property(player2, current_property)
        elif current_property.owner != player2:
            pay_rent(player2, current_property)

    # check winnen
    if has_won(player2):
        print(f"{player2.name} has won the game!")
        game_over = True

# ----------------------------------------------------------------------------------------------------------------------------

# EXTRA FUNCTIES

class Card:
    def __init__(self, text):
        self.text = text

# CHANCE + COMMUNITY CARDS
chance_cards = [
    Card("Advance to Go. Collect $200."),
    Card("Bank error in your favor. Collect $75."),
    Card("Go directly to Jail. Do not pass Go, do not collect $200."),
]

community_chest_cards = [
    Card("Get out of Jail Free. This card may be kept until needed or sold."),
    Card("Income tax refund. Collect $20."),
    Card("Go back to Illinois Avenue. If you pass Go, collect $200."),
]

# DRAW CARD
def draw_card(cards):
    return random.choice(cards)

# HANDLE CARD EFFECT 
def handle_chance_card(player, card):
    # nog niet klaar
    pass

# HANDLE CARD EFFECT 
def handle_community_chest_card(player, card):
    # nog niet klaar
    pass

# JAIL
def handle_jail(player):
    # nog niet klaar -> dubbel rollen etc 
    pass

# PROPERTY SELLING 
def auction_property(property):
    # nog niet klaar -> wanneer speler property moet verkopen ivm geen gel
    pass

# PROPERTY DEVELOPMENT 
def develop_property(property):
    # nog niet klaar -> houses/ hotels
    pass

