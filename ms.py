#!/usr/bin/python3

from game import Game
from consoleplayer import ConsolePlayer
from networkplayer import NetworkPlayer
import sys
import os

if __name__ == "__main__":
    print('''Minesweeper!

This is a clone of minesweeper.  To win, mark all the mines with a flag.
Select a tile by entering the row and column number, separated by a single
space, like this:

> 4 7

To flag or unflag a tile, enter "f" followed by the row an column:

> f 8 2

To quit, type "quit"

What type of game would you like to play?
a) Easy
b) Medium
c) Hard
''')
    while True:
        try:
            response = input("? ")
            if response in ["a", "b", "c", "quit"]:
                break
        except EOFError:
            sys.exit()
    if response == "quit":
        sys.exit()

    g = None
    if response == "a":
        g = Game(9, 9, 10)
    elif response == "b":
        g = Game(16, 16, 40)
    elif response == "c":
        g = Game(16, 30, 99)
    else:
        sys.exit()

    name = os.environ["USER"]
    g.addPlayer(ConsolePlayer(name))
    g.play()
