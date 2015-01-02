import sys

number_of_solutions = 0

def print_solution(board):
	global number_of_solutions 
	number_of_solutions += 1
	for i, row_val in enumerate(board):
		for j, val in enumerate(board[i]):
			if val == 1:
				sys.stdout.write(str(0) + " ")	
			else:
				sys.stdout.write(str(val) + " ")
		print 

def is_solution(queen):
	if queen != 8:
		return False
	else:
		return True


def next_possible_moves(board, queen):
	possible_moves = []
	for j, col_val in enumerate(board[queen]):
		if col_val == 0:
			possible_moves.append(j)
	return possible_moves

def fill_path(board):
	fill_elements = []
	# Reset the board
	for row in board:
		for j, val in enumerate(row):
			if val == 1:
				row[j] = 0
	
	for i, row_val in enumerate(board):
		for j, col_val in enumerate(board[i]):
			if col_val == 2:
				# Set the entire row to 1 except for the placed queen
				fill_elements.extend([(i,col_idx) for col_idx in range(8)  if col_idx != j ])

				# Set the entire column to 1
				fill_elements.extend([(row_idx,j) for row_idx in range(8) if row_idx != i])
				
				# Set the entire diaganol to 1
				fill_elements.extend(_get_diagonal_elements(i,j))

	for i,j in fill_elements:
		board[i][j] = 1

	return board							

def _get_diagonal_elements(i,j, square_side=8):
	diagonal_elements = []

	temp_i = i 
	temp_j = j
	while(temp_i-1 >= 0 and temp_j-1 >= 0 ):
		temp_i = temp_i - 1
		temp_j = temp_j - 1
		diagonal_elements.append((temp_i, temp_j))

	temp_i = i 
	temp_j = j
	while(temp_i-1 >= 0 and temp_j+1 < square_side):
		temp_i = temp_i - 1
		temp_j = temp_j + 1
		diagonal_elements.append((temp_i, temp_j))

	temp_i = i 
	temp_j = j
	while(temp_i+1 < square_side and temp_j-1 >=0):
		temp_i = temp_i + 1
		temp_j = temp_j - 1
		diagonal_elements.append((temp_i, temp_j))


	while(i+1 < square_side and j+1 < square_side):
		i = i + 1
		j = j + 1
		diagonal_elements.append((i, j))

	
	return diagonal_elements

def place_queen(board, row_index, column_index):
	board[row_index][column_index] = 2
	fill_path(board)
	return board

def unplace_queen(board, row_index, column_index):
	board[row_index][column_index] = 0
	fill_path(board)
	return board

def track_queen(board, queen):
	"""
	Backtracking algorithm for identify all possible solutions for placing a queen in chess board
	"""
	if (is_solution(queen)):
		print "==== Found solution ===== "		
		print_solution(board)
	else:
		possible_col_pos = next_possible_moves(board, queen)
		for col_idx in possible_col_pos:
			board = place_queen(board, queen, col_idx)
			board = track_queen(board, queen+1)
			board = unplace_queen(board, queen, col_idx)
		
	return board

# chess board 8 x 8 
board =  [[0 for i in range(8)] for j in range(8)]
track_queen(board, 0)
print "Total number of solutions " + str(number_of_solutions)
