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
print(f"{player1.name} - Money: ${player1.money}, Position: {player1.position}")
print(f"{player2.name} - Money: ${player2.money}, Position: {player2.position}")

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
dice_roll = roll_dice()
move_player(player1, dice_roll)
print(f"{player1.name} rolled a {dice_roll} and moved to position {player1.position}")

pass_go(player1)
print(f"{player1.name} passed Go and collected $200. Money: ${player1.money}")

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
player1.money = 1000  # player 1 minder money voor test 
purchase_property(player1, board[1])  # player 1 koopt Mediterranean Avenue
pay_rent(player1, board[1])  # player 1 betaald rent voor Mediterranean Avenue

