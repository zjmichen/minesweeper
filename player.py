from board import Board

class Player:
    def __init__(self, name):
        self.gamestate = Board(0, 0, 0)
        self.name = name

    def setBoard(self, x, y, mines):
        self.gamestate = Board(x, y, 0)
        self.gamestate.numMines = mines

    def getMove(self):
        return ["pick", 0, 0]

    def sendState(self, tiles, type="reveal"):
        for t in tiles:
            if type == "flag":
                self.gamestate.flag(t[0], t[1])
            else:
                self.gamestate.grid[t[0]][t[1]].value = t[2]
                self.gamestate.grid[t[0]][t[1]].isVisible = True

    def printState(self):
        print(self.name, ":", sep='')
        print(self.gamestate.guessNumLeft(), "mines left")
        self.gamestate.print()
