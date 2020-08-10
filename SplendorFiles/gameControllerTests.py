from gameController import *

print("Testing GameController Class.")
g = GameController()
assert len(g.TierOneCards) == 40 and len(g.TierOneOrder) == 40 and len(g.TierTwoCards) == 30 and len(g.TierTwoOrder) == 30 and len(g.TierThrCards) == 20 and len(g.TierThrOrder) == 20 \
and g.Players == [] and g.OneOnTable == [] and g.TwoOnTable == [] and g.ThrOnTable == [] and not g.Started and g.Coins == {}, "FAIL: Incorrect variable initialization."
print("Game controller constructor passed.")
g.AddPlayer("Eidan")
assert g.Players[0] is not None, "FAIL: Player Eidan not created."
assert g.Players[0].Name == "Eidan", "FAIL: Incorrect player name: " + g.Players[0].Name + ". Expected: Eidan"
g.AddPlayer()
assert g.Players[1] is not None, "FAIL: Player 2 not created."
assert g.Players[1].Name == "Player 2", "FAIL: Incorrect player name: " + g.Players[1].Name + ". Expected: Player 2"
g.AddPlayer()
g.AddPlayer()
g.AddPlayer()
assert len(g.Players) == 4, "FAIL: Added more than 4 players."
f = GameController()
f.StartGame()
f.AddPlayer()
assert len(f.Players) == 1, "FAIL: Added player after start of game." # Also confirms StartGame() adds a player if zero exist.
print("AddPlayers() method passed.")
g.DealCards()
assert len(g.OneOnTable) == 4 and len(g.TwoOnTable) == 4 and len(g.ThrOnTable) == 4, "FAIL: Incorrect number of cards dealt."
for tier in [g.OneOnTable, g.TwoOnTable, g.ThrOnTable]:
    for cardObj in tier:
        assert cardObj.Location == "Table", "FAIL: Card location not updated to Table."
print("DealCards() method passed.")
g = GameController()
g.StartGame()
assert g.Started, "FAIL: Game status unchanged."
assert len(g.OneOnTable) == 4 and len(g.TwoOnTable) == 4 and len(g.ThrOnTable) == 4, "FAIL: Cards were not dealt."
# TODO: test noble dealing.
assert g.Coins["gold"] == 5 and g.Coins["black"] == 7, "FAIL: Incorrect number of coins for a one-player game."
g = GameController()
g.AddPlayer()
g.AddPlayer()
g.StartGame()
assert g.Coins["gold"] == 5 and g.Coins["green"] == 4, "FAIL: Incorrect number of coins for a two-player game."
g = GameController()
g.AddPlayer()
g.AddPlayer()
g.AddPlayer()
g.StartGame()
assert g.Coins["gold"] == 5 and g.Coins["white"] == 5, "FAIL: Incorrect number of coins for a three-player game."
g = GameController()
g.AddPlayer()
g.AddPlayer()
g.AddPlayer()
g.AddPlayer()
g.StartGame()
assert g.Coins["gold"] == 5 and g.Coins["red"] == 7, "FAIL: Incorrect number of coins for a four-player game."
print("StartGame() method passed.")
