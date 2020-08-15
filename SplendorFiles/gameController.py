import random

# 3 letter vars for colors
blk = "black"
wht = "white"
blu = "blue"
grn = "green"
red = "red"
gld = "gold"
Colors = { blk : (0, 0, 0), wht : (255, 255, 255), blu : (0, 0, 255), \
    grn : (0, 255, 0), red : (255, 0, 0), gld : (255, 255, 0) }

# ID : [Tier, Points, Color, Black, White, Blue, Green, Red]
CardDictionary = { \
        # 1st Tier
         0 : [1, 0, blk, 0, 1, 1, 1, 1],  1 : [1, 0, wht, 1, 0, 1, 1, 1],  2 : [1, 0, blu, 1, 1, 0, 1, 1],  3 : [1, 0, grn, 1, 1, 1, 0, 1],  4 : [1, 0, red, 1, 1, 1, 1, 0], \
         5 : [1, 0, blk, 0, 1, 2, 1, 1],  6 : [1, 0, wht, 1, 0, 1, 2, 1],  7 : [1, 0, blu, 1, 1, 0, 1, 2],  8 : [1, 0, grn, 2, 1, 1, 0, 1],  9 : [1, 0, red, 1, 2, 1, 1, 0], \
        10 : [1, 0, blk, 0, 0, 0, 3, 0], 11 : [1, 0, wht, 0, 0, 3, 0, 0], 12 : [1, 0, blu, 3, 0, 0, 0, 0], 13 : [1, 0, grn, 0, 0, 0, 0, 3], 14 : [1, 0, red, 0, 3, 0, 0, 0], \
        15 : [1, 1, blk, 0, 0, 4, 0, 0], 16 : [1, 1, wht, 0, 0, 0, 4, 0], 17 : [1, 1, blu, 0, 0, 0, 0, 4], 18 : [1, 1, grn, 4, 0, 0, 0, 0], 19 : [1, 1, red, 0, 4, 0, 0, 0], \
        20 : [1, 0, blk, 0, 2, 2, 0, 1], 21 : [1, 0, wht, 1, 0, 2, 2, 0], 22 : [1, 0, blu, 0, 1, 0, 2, 2], 23 : [1, 0, grn, 2, 0, 1, 0, 2], 24 : [1, 0, red, 2, 2, 0, 1, 0], \
        25 : [1, 0, blk, 0, 2, 0, 2, 0], 26 : [1, 0, wht, 2, 0, 2, 0, 0], 27 : [1, 0, blu, 2, 0, 0, 2, 0], 28 : [1, 0, grn, 0, 0, 2, 0, 2], 29 : [1, 0, red, 0, 2, 0, 0, 2], \
        30 : [1, 0, blk, 0, 0, 0, 2, 1], 31 : [1, 0, wht, 1, 0, 0, 0, 2], 32 : [1, 0, blu, 2, 1, 0, 0, 0], 33 : [1, 0, grn, 0, 2, 1, 0, 0], 34 : [1, 0, red, 0, 0, 2, 1, 0], \
        35 : [1, 0, blk, 1, 0, 0, 1, 3], 36 : [1, 0, wht, 1, 3, 1, 0, 0], 37 : [1, 0, blu, 0, 0, 1, 3, 1], 38 : [1, 0, grn, 0, 1, 3, 1, 0], 39 : [1, 0, red, 3, 1, 0, 0, 1], \
        # 2nd Tier 
        40 : [2, 3, blk, 6, 0, 0, 0, 0], 41 : [2, 3, wht, 0, 6, 0, 0, 0], 42 : [2, 3, blu, 0, 0, 6, 0, 0], 43 : [2, 3, grn, 0, 0, 0, 6, 0], 44 : [2, 3, red, 0, 0, 0, 0, 6], \
        45 : [2, 1, blk, 0, 3, 2, 2, 0], 46 : [2, 1, wht, 2, 0, 0, 3, 2], 47 : [2, 1, blu, 0, 0, 2, 2, 3], 48 : [2, 1, grn, 2, 2, 3, 0, 0], 49 : [2, 1, red, 3, 2, 0, 0, 2], \
        50 : [2, 1, blk, 2, 3, 0, 3, 0], 51 : [2, 1, wht, 0, 2, 3, 0, 3], 52 : [2, 1, blu, 3, 0, 2, 3, 0], 53 : [2, 1, grn, 0, 3, 0, 2, 3], 54 : [2, 1, red, 3, 0, 3, 0, 2], \
        55 : [2, 2, blk, 0, 5, 0, 0, 0], 56 : [2, 2, wht, 0, 0, 0, 0, 5], 57 : [2, 2, blu, 0, 0, 5, 0, 0], 58 : [2, 2, grn, 0, 0, 0, 5, 0], 59 : [2, 2, red, 5, 0, 0, 0, 0], \
        60 : [2, 2, blk, 0, 0, 1, 4, 2], 61 : [2, 2, wht, 2, 0, 0, 1, 4], 62 : [2, 2, blu, 4, 2, 0, 0, 1], 63 : [2, 2, grn, 1, 4, 2, 0, 0], 64 : [2, 2, red, 0, 1, 4, 2, 0], \
        65 : [2, 2, blk, 0, 0, 0, 5, 3], 66 : [2, 2, wht, 3, 0, 0, 0, 5], 67 : [2, 2, blu, 0, 5, 3, 0, 0], 68 : [2, 2, grn, 0, 0, 5, 3, 0], 69 : [2, 2, red, 5, 3, 0, 0, 0], \
        # 3rd Tier
        70 : [3, 3, blk, 0, 3, 3, 5, 3], 71 : [3, 3, wht, 3, 0, 3, 3, 5], 72 : [3, 3, blu, 5, 3, 0, 3, 3], 73 : [3, 3, grn, 3, 5, 0, 3, 3], 74 : [3, 3, red, 3, 3, 5, 3, 0], \
        75 : [3, 4, blk, 3, 0, 0, 3, 6], 76 : [3, 4, wht, 6, 3, 0, 0, 3], 77 : [3, 4, blu, 3, 6, 3, 0, 0], 78 : [3, 4, grn, 0, 3, 6, 3, 0], 79 : [3, 4, red, 0, 0, 3, 6, 3], \
        80 : [3, 4, blk, 0, 0, 0, 0, 7], 81 : [3, 4, wht, 7, 0, 0, 0, 0], 82 : [3, 4, blu, 0, 7, 0, 0, 0], 83 : [3, 4, grn, 0, 0, 7, 0, 0], 84 : [3, 4, red, 0, 0, 0, 7, 0], \
        85 : [3, 5, blk, 3, 0, 0, 0, 7], 86 : [3, 5, wht, 7, 3, 0, 0, 0], 87 : [3, 5, blu, 0, 7, 3, 0, 0], 88 : [3, 5, grn, 0, 0, 7, 3, 0], 89 : [3, 5, red, 0, 0, 0, 7, 3] }

# Tracks the game state.    
class GameController:

    # Constructs a new game class.
    def __init__(self):
        self.TierOneCards = {card : Card(*info) for card, info in CardDictionary.items() if info[0] == 1}
        self.TierOneOrder = random.sample(list(self.TierOneCards.keys()), len(self.TierOneCards))
        self.TierTwoCards = {card : Card(*info) for card, info in CardDictionary.items() if info[0] == 2}
        self.TierTwoOrder = random.sample(list(self.TierTwoCards.keys()), len(self.TierTwoCards))
        self.TierThrCards = {card : Card(*info) for card, info in CardDictionary.items() if info[0] == 3}
        self.TierThrOrder = random.sample(list(self.TierThrCards.keys()), len(self.TierThrCards))
        self.Players = []
        self.OneOnTable = []
        self.TwoOnTable = []
        self.ThrOnTable = []
        self.Started = False
        self.Coins = {}

    # Adds a player to the game.
    def AddPlayer(self, name = ""):
        # Don't add a player when the game has already started or when the table is already full.
        if not self.Started and not len(self.Players) >= 4:
            # Add a "Player #" if no name is provided.
            if name == "":
                name = "Player " + str(len(self.Players) + 1)
            self.Players.append(Player(name))

    # Deal out 4 cards of each tier, unless that tier has been depleted already.
    def DealCards(self):
        while len(self.OneOnTable) < 4 and len(self.TierOneOrder) > 0:
            cardId = self.TierOneOrder.pop()
            cardObj = self.TierOneCards[cardId]
            cardObj.UpdateLocation("Table")
            self.OneOnTable.append(cardObj)
                   
        while len(self.TwoOnTable) < 4 and len(self.TierTwoOrder) > 0:
            cardId = self.TierTwoOrder.pop()
            cardObj = self.TierTwoCards[cardId]
            cardObj.UpdateLocation("Table")
            self.TwoOnTable.append(cardObj)
            
        while len(self.ThrOnTable) < 4 and len(self.TierThrOrder) > 0:
            cardId = self.TierThrOrder.pop()
            cardObj = self.TierThrCards[cardId]
            cardObj.UpdateLocation("Table")
            self.ThrOnTable.append(cardObj)

    # Start the game.
    def StartGame(self):
        # Default to 1 player (testing).
        if len(self.Players) == 0:
            self.AddPlayer()
        self.DealCards()
        quantity = 7
        if len(self.Players) == 2:
            quantity = 4
        elif len(self.Players) == 3:
            quantity = 5
        self.Coins = { color : quantity for color in [blk, wht, blu, red, grn] } 
        self.Coins[gld] = 5
        # TODO: Deal out noble tiles.
        self.Started = True

# Class representing a card
class Card:

    def __init__(self, tier, color, points = 0,
                 black = 0, white = 0,  blue = 0, green = 0, red = 0):
        self.Tier = tier
        self.Color = color
        self.Points = points
        self.Cost = {"black": black,
                     "white" : white,
                     "blue" : blue,
                     "green": green,
                     "red" : red}
        self.Cost = {key:val for key, val in self.Cost.items() if val!= 0}
        self.Location = "Deck"

    def UpdateLocation(self, newLocation):
        if (self.Location == "Deck" and newLocation == "Table") or (self.Location == "Table" and (newLocation == "Reserve" or newLocation == "Tableau")) or (self.Location == "Reserve" and newLocation == "Tableau"):
            self.Location = newLocation

# Class representing a player
class Player:

    def __init__(self, name):
        self.Name = str(name)
        self.Coins = { color : 0 for color in [blk, wht, blu, red, grn, gld] }
        self.Cards = { color : 0 for color in [blk, wht, blu, red, grn] }
        self.Score = 0
        self.Reserve = []

    def GetAvailableCards(self, game):
        return self.Reserve + game.OneOnTable + game.TwoOnTable + game.ThreeOnTable
