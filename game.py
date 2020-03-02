# Filename: game.py

from itertools import cycle
from turtle import onscreenclick

import constants
import players
from graphic_utils import announce
from board import Board
from logic import GameLogic
"""check 2"""

# constants for costume players:
# player type:
HUMAN = constants.HUMAN
COMPUTER = constants.COMPUTER
# player sign:
X_SIGN = constants.X_SIGN
O_SIGN = constants.O_SIGN


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
		specify the sign (X_SIGN or O_SIGN)
		"""
		
		board_size = 3 # 3 squares each row/column.
		self._board = Board(board_size, sqaure_size)
		self._logic = GameLogic(self._board)
		self._game_is_over = False
		
		# create a circular list of players
		players_list = []
		players_list.append(players.create_new_player(player1[0],player1[1],
			self._board))
		players_list.append(players.create_new_player(player2[0],player2[1],
			self._board))
		
		self.players = cycle(players_list)
		self.current_player = next(self.players)
		
		# draw gird
		self._board.draw_grid()
	
	def run(self):
		"""Main loop of events."""
		
		# only ComPlayer allow to enter this loop.
		while isinstance(self.current_player, players.ComPlayer) and \
			not self._game_is_over:
			self.current_player.play()			
			self._end_turn()
		
		if not self._game_is_over:
			# its human turn. wait for a click from the user
			onscreenclick(self._on_click)
	
	def _on_click(self, x, y):
		"""Defines what happens in a human turn."""
		
		# convert coordinates to (row, column)
		row = int(y / self._board.sqaure_size)
		column = int(x / self._board.sqaure_size)
		
		if self._board.square_is_empty(row, column):
			# stop react to farther clicks
			onscreenclick(None)
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
	
	def _end_game(self, msg):
		"""print who wins and disable farther playing."""
		
		self._game_is_over = True
		announce(self._board.size, self._board.sqaure_size ,msg)
		
		# disable farther clicking on the screen
		onscreenclick(None)
	


