# Filename: game.py

from board import Board

class GameLogic():
	"""Checks winning/losing state for the given board and player."""
	
	def __init__(self, board: Board):
		self._board = board
		self._seq_to_win = 3
	
	def is_player_winner(self, player):
		"""Checks winning state for the given player."""
		
		is_player_winner = False
		
		if self._has_row_winning(player):
			is_player_winner = True
		
		elif self._has_column_winning(player):
			is_player_winner = True
		
		elif self._has_diagonal_winning(player):
			is_player_winner = True
		
		return is_player_winner
	
	def _has_row_winning(self, player):
		"""Checks wheather player has a row winning."""
		
		counter = 0
		for row in range(self._board.size):
			for column in range(self._board.size):
				if self._board.get_sign(row, column) is player:
					counter += 1
				else:
					counter = 0
				
				if counter == self._seq_to_win:
					return True
			
			# zero the counter before checking the next line
			counter = 0

		return False

	def _has_column_winning(self, player):
		"""Checks wheather player has a column winning."""
		
		counter = 0
		for column in range(self._board.size):
			for row in range(self._board.size):
				if self._board.get_sign(row, column) is player:
					counter += 1
				else:
					counter = 0
				
				if counter == self._seq_to_win:
					return True
			
			# zero the counter before checking the next line
			counter = 0

		return False

	def _has_diagonal_winning(self, player):
		"""Checks wheather player has a slant winning."""
		
		counter = 0
		
		# check slant 1
		for row in range(self._board.size):
			if self._board.get_sign(row, row) is player:
				counter += 1
			else:
				counter = 0
			
			if counter == self._seq_to_win:
				return True

		# check slant 2
		counter = 0
		for row in range(self._board.size):
			if self._board.get_sign(row, self._board.size - row - 1) is player:
				counter += 1
			else:
				counter = 0
			
			if counter == self._seq_to_win:
				return True
		
		return False


