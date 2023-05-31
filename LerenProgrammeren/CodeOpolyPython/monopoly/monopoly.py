# MONOPOLY

class Property:
    def __init__(self, name, price, rent):
        self.name = name
        self.price = price
        self.rent = rent

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
