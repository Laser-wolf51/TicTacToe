# Filename: main.py

"""
Tic Tac Toe

This program implements a X/O (Tic Tac Toe) game with an optional unbeatable 
computer player.

This implementaion is based on 'turtle' graphics library and the idea of making 
this game was inspired from 'Free Python Games' - a collection of games 
programming challanges in pyhon:
http://www.grantjenks.com/docs/freegames/

Enjoy :)
"""

import turtle
import game

SQAURE_SIZE = 150
BOARD_SIZE = 3
WND_SIZE = SQAURE_SIZE * BOARD_SIZE

# configure screen + turtle
turtle.setup(WND_SIZE, WND_SIZE)
turtle.setworldcoordinates(0,0, WND_SIZE, WND_SIZE)
turtle.title("X / O")
# turtle.tracer(False)


# set the board
game = game.Game(sqaure_size=SQAURE_SIZE,
	player2=(game.COMPUTER,'X'),
	player1=(game.HUMAN,'O'))
game.run()
turtle.done() # keeps the screen on.


# TODO: Advanced features:
# TODO: add buttons like human/AI and first player sign ('X'/'O').
# TODO: main loop. sleeps when its human turn until the click. how?
# TODO: board - overload the operator [][]
# TODO: variable board size + rules.


# How to add buttons:
# crate the window with TK, then use rawturtle.
# https://stackoverflow.com/questions/44653500/integrate-turtle-module-with-tkinter-canvas

# How to compile into exe file:
# auto-py-to-exe
