# Filename: players.py

import abc

from .constants import *
from .board import Board


def create_new_player(type_, sign, board: Board):
	"""
	Create a new player of type 'type_' with sign 'sign'.
	'type_' must be HUMAN or COMPUTER.
	'sign' must be X_SIGN or O_SIGN.
	Otherwise - raises an exception.
	"""
	
	# check input
	assert type_ is HUMAN or type_ is COMPUTER, 'wrong player type'
	assert sign is X_SIGN or sign is O_SIGN, 'wrong sign'
	assert isinstance(board, Board)
	
	if type_ is HUMAN:
		return HumanPlayer(sign, board)
	else:
		return ComPlayer(sign, board)
	

class Player(abc.ABC):
	"""Abstract class, common to all kinds of players."""
	
	def __init__(self, sign, board: Board):
		self._sign = sign
		self._board = board
	
	@abc.abstractmethod
	def play(self, args):
		pass
	
	def get_sign(self):
		"""Returns the sign of the player."""
		
		return self._sign


class HumanPlayer(Player):
	"""Crate an object represinting a human player."""
	
	def __init__(self, sign, board: Board):
		
		# init base class
		super().__init__(sign, board)
		
		# checks the rival sign:
		if sign is X_SIGN:
			self._rival = O_SIGN
		elif sign is O_SIGN:
			self._rival = X_SIGN
	
	def play(self):
		"""Performs a single turn"""
		
		# not implemented for now.
		pass


class ComPlayer(Player):
	"""
	Create an unbeatable computer player and defines its behaviour.
	Note: suitable only for a standard tic tac toe board.
	"""
	
	def __init__(self, sign, board: Board):
		
		# init base class
		super().__init__(sign, board)
		
		# checks the rival sign:
		if sign is X_SIGN:
			self._rival = O_SIGN
		elif sign is O_SIGN:
			self._rival = X_SIGN
	
	def play(self):
		"""Performs a single turn"""
		
		# preference 1: populate center
		if self._board.square_is_empty(1,1):
			self._board.put_sign(1, 1, self._sign)
		
		# preference 2: try instant winning
		elif self._instant_winning() == "SUCCESS":
			return
		
		# preference 3: block instant losing
		elif self._instant_block() == "SUCCESS":
			return
		
		# preference 4: if its turn 4 + rival in 2 opposite corners
		elif self._is_special_case():
			self._solve_special_case()
			return
		
		# preference 5: try populate corners
		elif self._populate_corner() == "SUCCESS":
			return
			
		# preference 6: fill wherever possible
		else:
			self._fill_first_free()
			# Note: may produce Exception when board is full
	
	###### INTERNAL FUNCTIONS ########
	def _instant_winning(self):
		"""
		Try to win in 1 turn. If succeeded - returns 'SUCCEESS', 'FAIL'
		otherwise.
		"""
		
		sings_counter = {X_SIGN: 0, O_SIGN: 0, None: 0}
		
		# checks a rows winning option
		for row in range(self._board.size):
			for column in range(self._board.size):
				sings_counter[self._board.get_sign(row,column)] += 1
			
			if sings_counter[self._sign] == 2 and sings_counter[None] == 1:
				self._put_in_row(row)
				return "SUCCESS"
			
			sings_counter = {X_SIGN: 0, O_SIGN: 0, None: 0}
		
		sings_counter = {X_SIGN: 0, O_SIGN: 0, None: 0}
		
		# checks columns winning option
		for column in range(self._board.size):
			for row in range(self._board.size):
				sings_counter[self._board.get_sign(row,column)] += 1
			
			if sings_counter[self._sign] == 2 and sings_counter[None] == 1:
				self._put_in_column(column)
				return "SUCCESS"
			
			sings_counter = {X_SIGN: 0, O_SIGN: 0, None: 0}
		
		sings_counter = {X_SIGN: 0, O_SIGN: 0, None: 0}
		
		# checks slant 1 winning option
		for row in range(self._board.size):
			sings_counter[self._board.get_sign(row,row)] += 1
		
		if sings_counter[self._sign] == 2 and sings_counter[None] == 1:
			self._put_in_slant1()
			return "SUCCESS"
		
		sings_counter = {X_SIGN: 0, O_SIGN: 0, None: 0}
		
		# checks slant 2 winning option
		for row in range(self._board.size):
			sings_counter[self._board.get_sign(row, self._board.size-row-1)] += 1
		
		if sings_counter[self._sign] == 2 and sings_counter[None] == 1:
			self._put_in_slant2()
			return "SUCCESS"
		
		return 'FAIL'
	
	def _instant_block(self):
		"""
		Checks if there is a the rival can win in the next turn. If he can -
		block the rival and returns 'SUCCEESS', 'FAIL' otherwise.
		"""
		
		sings_counter = {X_SIGN: 0, O_SIGN: 0, None: 0}
		
		# checks a rows blocking option
		for row in range(self._board.size):
			for column in range(self._board.size):
				sings_counter[self._board.get_sign(row,column)] += 1
			
			if sings_counter[self._rival] == 2 and sings_counter[None] == 1:
				self._put_in_row(row)
				return "SUCCESS"
			
			sings_counter = {X_SIGN: 0, O_SIGN: 0, None: 0}
		
		sings_counter = {X_SIGN: 0, O_SIGN: 0, None: 0}
		
		# checks columns blocking option
		for column in range(self._board.size):
			for row in range(self._board.size):
				sings_counter[self._board.get_sign(row,column)] += 1
			
			if sings_counter[self._rival] == 2 and sings_counter[None] == 1:
				self._put_in_column(column)
				return "SUCCESS"
			
			sings_counter = {X_SIGN: 0, O_SIGN: 0, None: 0}
		
		sings_counter = {X_SIGN: 0, O_SIGN: 0, None: 0}
		
		# checks slant 1 blocking option
		for row in range(self._board.size):
			sings_counter[self._board.get_sign(row,row)] += 1
		
		if sings_counter[self._rival] == 2 and sings_counter[None] == 1:
			self._put_in_slant1()
			return "SUCCESS"
		
		sings_counter = {X_SIGN: 0, O_SIGN: 0, None: 0}
		
		# checks slant 2 blocking option
		for row in range(self._board.size):
			sings_counter[self._board.get_sign(row, self._board.size-row-1)] += 1
		
		if sings_counter[self._rival] == 2 and sings_counter[None] == 1:
			self._put_in_slant2()
			return "SUCCESS"
		
		return 'FAIL'
	
	def _is_special_case(self):
		"""
		Checks if its a special case the the rest of the algorithm cannot
		handle.
		"""
		
		if self._board.count_occupied_squares() == 3 and \
			self._rival_in_opposite_corners():
			return True
		
		else: return False
	
	def _rival_in_opposite_corners(self):
		if (self._board.get_sign(0,0) is self._rival and \
			self._board.get_sign(2,2) is self._rival) or \
			(self._board.get_sign(0,2) is self._rival and \
			self._board.get_sign(2,0) is self._rival):
			return True
		
		else: return False
	
	def _solve_special_case(self):
		"""Prevent the opponent from winning in the special case."""
		self._board.put_sign(1, 0, self._sign)
	
	def _populate_corner(self):
		"""
		Try to populate the first free corner. If succeeded - returns 'SUCCESS',
		or 'FAIL' otherwise.
		"""
		
		if self._board.square_is_empty(0, 0):
			self._board.put_sign(0, 0, self._sign)
			return 'SUCCESS'
			
		elif self._board.square_is_empty(2, 0):
			self._board.put_sign(2, 0, self._sign)
			return 'SUCCESS'
		
		elif self._board.square_is_empty(0, 2):
			self._board.put_sign(0, 2, self._sign)
			return 'SUCCESS'
		
		elif self._board.square_is_empty(0, 0):
			self._board.put_sign(2, 2, self._sign)
			return 'SUCCESS'
		
		else: return 'FAIL'
	
	def _fill_first_free(self):
		"""
		Traverse the board and populate the first free square.
		If none is found - raises an exception.
		"""
		
		for row in range(self._board.size):
			for column in range(self._board.size):
				if self._board.square_is_empty(row, column):
					self._board.put_sign(row, column, self._sign)
					return
		
		# if no empty square was found - raise a ComPlayerError
		raise ComPlayer.ComPlayerError('board is full!!')
	
	def _put_in_row(self, row):
		for column in range(self._board.size):
			if self._board.square_is_empty(row, column):
				self._board.put_sign(row, column, self._sign)
				return
		
		# if no empty square was found - raise a ComPlayerError
		raise ComPlayer.ComPlayerError('row is full!!') 
	
	def _put_in_column(self, column):
		for row in range(self._board.size):
			if self._board.square_is_empty(row, column):
				self._board.put_sign(row, column, self._sign)
				return
		
		# if no empty square was found - raise a ComPlayerError
		raise ComPlayer.ComPlayerError('column is full!!') 
	
	def _put_in_slant1(self):
		for row in range(self._board.size):
			if self._board.square_is_empty(row, row):
				self._board.put_sign(row, row, self._sign)
				return
		
		# if no empty square was found - raise a ComPlayerError
		raise ComPlayer.ComPlayerError('slant1 is full!!') 
		
	def _put_in_slant2(self):
		for row in range(self._board.size):
			if self._board.square_is_empty(row, self._board.size - row - 1):
				self._board.put_sign(row, self._board.size-row-1, self._sign)
				return
		
		# if no empty square was found - raise a ComPlayerError
		raise ComPlayer.ComPlayerError('slant2 is full!!') 
	
	
	class ComPlayerError(Exception):
		"""Exception raised when ComPlayerError meets an unexcpected problem."""
		
		def __init__(self, message):
			self.message = message
	