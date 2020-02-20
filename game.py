# Filename: game.py

from itertools import cycle
from turtle import onscreenclick

import players
from graphic_utils import announce
from board import Board
from logic import GameLogic
"""check 2"""

# constant player types:
HUMAN = 'h'
COMPUTER = 'c'

class Game():
	"""
	The Game object handles all the game control, including the players, the 
	board, and the game logics.
	
	Note: a turtle screen must be defined before creating a game object.
	"""
	def __init__(self, player1: tuple, player2: tuple, sqaure_size=150):
		"""
		player1, player2 are tuples. the first item in each tuple specify
		the type of player: use the variables HUMAN or COMPUTER. the second item
		specify the sign ('X' or 'O')
		"""
		
		board_size = 3 # 3 squares each row/column.
		self._sqaure_size = sqaure_size
		self._board = Board(board_size, sqaure_size)
		self._logic = GameLogic(self._board)
		self._game_is_over = False
		
		# create a circular list of players
		players_list = []
		
		# create player 1
		if player1[0] is HUMAN:
			players_list.append(players.HumanPlayer(player1[1], self._board))
		elif player1[0] is COMPUTER:
			players_list.append(players.ComPlayer(player1[1], self._board))
		
		# create player 2
		if player2[0] is HUMAN:
			players_list.append(players.HumanPlayer(player2[1], self._board))
		elif player2[0] is COMPUTER:
			players_list.append(players.ComPlayer(player2[1], self._board))
			
		self.players = cycle(players_list)
		self.current_player = next(self.players)
		
		# define behaviour on click
		onscreenclick(self._on_click)
		self._board.draw_grid()
	
	def run(self):
		"""Main loop of events."""
		
		# only ComPlayer allow to enter this loop.
		while (not self._game_is_over) and isinstance(self.current_player, 
			players.ComPlayer):
			self.current_player.play()			
			self._end_turn()
		pass
	
	def _on_click(self, x, y):
		"""Defines what happens in a human turn."""
		
		# convert coordinates to (row, column)
		row = int(y / self._sqaure_size)
		column = int(x / self._sqaure_size)
		
		if self._board.square_is_empty(row, column):
			self._board.put_sign(row, column, self.current_player.get_sign())
			self._end_turn()
			self.run()
	
	def _end_turn(self):
		"""Checks winning/draw condition, and switch turn to the next player."""
		
		# checks winning
		if self._logic.is_player_winner(self.current_player.get_sign()):
			self._end_game(self.current_player.get_sign() + 'Wins!!')
			return
		
		# checks draw
		elif self._board.is_full():
			self._end_game('Its a DRAW')
			return
		
		# switch turn to the next player
		self.current_player = next(self.players)
		pass
	
	def _end_game(self, msg):
		"""print who wins and disable farther playing."""
		
		self._game_is_over = True
		announce(self._board.size, self._sqaure_size ,msg)
		
		# disable farther clicking on the screen
		onscreenclick(None)
	


