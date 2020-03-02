# Filename: main.py

"""
Tic Tac Toe

A pythonic OOD implementation for 'X/O' (Tic Tac Toe) game with an optional
unbeatable computer player.
Based on 'turtle' graphics library.

Enjoy :)
"""

import turtle
from game import *

# constants
SQAURE_SIZE = 150
BOARD_SIZE = 3
WND_SIZE = SQAURE_SIZE * BOARD_SIZE

# configure screen + turtle
turtle.setup(WND_SIZE, WND_SIZE)
turtle.setworldcoordinates(0,0, WND_SIZE, WND_SIZE)
turtle.title("X / O")
# turtle.tracer(False) # Turn On/Off the tracer animation

# set the board
game = Game(sqaure_size=SQAURE_SIZE,
	player1=(HUMAN, O_SIGN),
	player2=(COMPUTER, X_SIGN))

# starts the game
game.run()

# keeps the game window open
turtle.done()





