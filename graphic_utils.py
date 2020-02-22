# Filename: graphic_utils.py
"""
Contains some usefull graphic functions of Tic Tac Toe files.
"""


import turtle

def draw_line(a, b, x, y):
    """Draw line from `(a, b)` to `(x, y)`."""
    
    turtle.up()
    turtle.goto(a, b)
    turtle.down()
    turtle.goto(x, y)
    turtle.up()  # stop drawing, pull pen up.

def draw_x(sqaure_size, row, column):
		"""Draw X player."""
		
		turtle.pen(pensize=5, pencolor="red")

		# calc X limits
		left_lim = (column + 0.1) * sqaure_size
		right_lim = (column + 0.9) * sqaure_size
		bottom_lim = (row + 0.1) * sqaure_size
		top_lim = (row + 0.9) * sqaure_size

		# draw
		draw_line(left_lim, top_lim, right_lim, bottom_lim)
		draw_line(right_lim, top_lim, left_lim, bottom_lim)

def draw_o(sqaure_size, row, column):
		"""Draw O player."""
		
		turtle.pen(pensize=5, pencolor="blue")

		# calc middle + radius
		midx = (column + 0.5) * sqaure_size
		midy = (row + 0.5) * sqaure_size
		radius = sqaure_size * 0.45

		turtle.goto(midx, midy - radius)
		turtle.down()
		turtle.circle(radius)
		turtle.up()

def draw_grid(board_size, sqaure_size):
    """Draw board grid."""
    
    board_len = sqaure_size * board_size
    two_sqaures = sqaure_size * 2
    sqaure = sqaure_size
    
    # vertical
    draw_line(sqaure, board_len, sqaure, 0)
    draw_line(two_sqaures, board_len, two_sqaures, 0)
    
    # horizontal
    draw_line(0, two_sqaures, board_len, two_sqaures)
    draw_line(0, sqaure, board_len, sqaure)

def announce(board_size, sqaure_size, msg):
    """Print the string 'msg' in the middle of the screen."""
    
    # get the turtle to the middle
    midx = sqaure_size * board_size / 2
    midy = sqaure_size * board_size / 2
    turtle.goto(midx, midy)
    turtle.down()
    
    # print final msg
    turtle.write(msg, align="center", font=("Arial", 30, "normal"))
    turtle.up()
    
    return
