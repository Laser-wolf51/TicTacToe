# Filename: board.py

from . import graphic_utils
from .constants import *

class Board():
	"""
	Mannages the squares and their content, including drawing their content.
	"""	
	
	def __init__(self, board_size, sqaure_size):
		
		# public attributes
		self.size = board_size
		self.sqaure_size = sqaure_size
		
		# create a 2D array of Squares
		self._table = [[Square() for y in range(board_size)]
								for x in range(board_size)]
		
	def get_sign(self, row, column):
		"""Returns the sign currently occupies the given square"""
		
		return self._table[row][column].get_content()
	
	def square_is_empty(self, row, column):
		"""Returns True if the given square is empty"""
		
		return self._table[row][column].is_empty()
	
	def is_full(self):
		""" returns True if the board is full, and False otherwise."""
		
		for row in range(self.size):
			for column in range(self.size):
				if self._table[row][column].is_empty():
					return False
		return True
	
	def put_sign(self, row, column, sign):
		"""
		if the square reffered by ('row','column') is empty - places 'sign' 
		inside it and draws the 'sign'. otherwise - throws an exception.
		"""
		square = self._table[row][column]
		
		if square.is_empty():
			square.set_content(sign)
			sign = square.get_content()
			
			if sign is X_SIGN:
				graphic_utils.draw_x(self.sqaure_size, row, column)
				pass
			
			elif sign is O_SIGN:
				graphic_utils.draw_o(self.sqaure_size, row, column)
			
			else:
				raise BoardError('board: uknown sign')
		
		else:
			raise BoardError('board: square occupied')
	
	def draw_grid(self):
		"""Draw board grid."""
		
		graphic_utils.draw_grid(self.size, self.sqaure_size)
	
	def count_occupied_squares(self):
		"""returns the number of occupied squares in the board."""
		
		counter = 0
		
		for row in range(self.size):
			for column in range(self.size):
				if self._table[row][column].is_occupied():
					counter += 1
		
		return counter
	
	class BoardError(Exception):
		"""Exception raised when trying to put a sign in the board."""
		
		def __init__(self, message):
			self.message = message



class Square():
	"""
	Mannages the content of a specific sqaure.
	"""
	def __init__(self):
		self._content = None  # can have None/X_SIGN/O_SIGN.
	
	def get_content(self):
		return self._content
	
	def set_content(self, val):
		self._content = val
	
	def is_empty(self):
		return self._content is None
	
	def is_occupied(self):
		return self._content is not None
