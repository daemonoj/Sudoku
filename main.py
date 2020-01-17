
"""	Creates a predefined Sudoku
	The missing values are represented as 0(Zeroes).
	Returns a double dimension matrix of size 9x9
	Also prints the original Sudoku
""" 
def create_sudoku():
	sudoku = [[0,0,0,2,6,0,7,0,1],
			  [6,8,0,0,7,0,0,9,0],
			  [1,9,0,0,0,4,5,0,0],
			  [8,2,0,1,0,0,0,4,0],
			  [0,0,4,6,0,2,9,0,0],
			  [0,5,0,0,0,3,0,2,8],
			  [0,0,9,3,0,0,0,7,4],
			  [0,4,0,0,5,0,0,3,6],
			  [7,0,3,0,1,8,0,0,0]]
	print_sudoku(sudoku)
	return sudoku


"""
	Takes a Sudoku as an argument
	Prints the given Sudoku on the terminal.
	The Zeroes are replaced by blanks.
"""
def print_sudoku(sudoku):
	print('-----------------------------------')
	for arr in sudoku:
		print('|' + ' | '.join(str(x) if x != 0 else ' ' for x in arr ) + '|')
		print('-----------------------------------')

"""
	Checks whether a given cell is empty or not
"""
def isEmpty(x):
	if x == 0:
		return True
	return False

# checks if the assumed solution is already presnt in the row or not
# takes 3 arguments
# number is the assumed solution for the cell
# row is the row number of the cell
# sudoku is the current solved table
def check_row(number, row, sudoku):
	for i in range(0,9):
		if number == sudoku[i][row]:
			return False

	return True

# checks if the assumed solution is already presnt in the column or not
# takes 3 arguments
# number is the assumed solution for the cell
# column is the column numberof the cell
# sudoku is the current solved table
# returns boolean representing whether value is presnt or not
def check_column(number, column,sudoku):
	for i in range(0,9):
		if number == sudoku[column][i]:
			return False

	return True

#checks if the assumed solution is already present in the block or not
# takes 4 arguments
# number is the assumed solution for the cell
# column is the column numberof the cell
# row is the row number of the cell
# sudoku is the current solved table
# returns boolean representing whether value is presnt or not
def check_block(number,row,column,sudoku):
	#Block 1
	if row < 3 and column < 3:
		for i in range(0,3):
			for j in range(0,3):
				if number == sudoku[i][j]:
					return False
	#Block 2
	elif row < 6 and column < 3:
		for i in range(0,3):
			for j in range(3,6):
				if number == sudoku[i][j]:
					return False
	#Block 3
	elif row < 9 and column < 3:
		for i in range(0,3):
			for j in range(6,9):
				if number == sudoku[i][j]:
					return False
	#Block 4
	elif row < 3 and column < 6:
		for i in range(3,6):
			for j in range(0,3):
				if number == sudoku[i][j]:
					return False
	#Block 5
	elif row < 6 and column < 6:
		for i in range(3,6):
			for j in range(3,6):
				if number == sudoku[i][j]:
					return False
	#Block 6
	elif row < 9 and column < 6:
		for i in range(3,6):
			for j in range(6,9):
				if number == sudoku[i][j]:
					return False
	#Block 7
	elif row < 3 and column < 9:
		for i in range(6,9):
			for j in range(0,3):
				if number == sudoku[i][j]:
					return False
	#Block 8
	elif row < 6 and column < 9:
		for i in range(6,9):
			for j in range(3,6):
				if number == sudoku[i][j]:
					return False
	#Block 9
	elif row < 9 and column < 9:
		for i in range(6,9):
			for j in range(6,9):
				if number == sudoku[i][j]:
					return False
	return True



"""
	Takes a Sudoku as an argument
	Solves the given Sudoku

"""
def solve_sudoku(sudoku):
	# creating a list to store all the positions that have been solved
	# this will also be used to backtrack in case solution isnt found
	empty_list = []
	# i will represent the column number here
	i = 0
	# j will represent the row number here
	j = 0
	# k is the solution value for any particular unsolved cell
	k = 1
	#infinite loop
	# TODO:  @me try to make this loop finite.
	while True:
		#check if the cell is empty or filled
		if isEmpty(sudoku[i][j]):
			# infinite loop to go through the solution values i.e. 1-9
			# this loop runs till all the values uptill that point are filled and
			# satisfy the solution
			while True:
				print('Checking for Value: ',k)
				print('At location: ', i, j)
				# if a solution value passes all the checks
				# row check column check and block check
				# we fill that number to the cell and move onto the next empty cell
				# also append the cell location to the empty list
				if check_row(k,j,sudoku) and check_column(k,i,sudoku) and check_block(k,j,i,sudoku):
					sudoku[i][j] = k
					empty_list.append((i,j))
					# resetting the value of k
					# so that it starts checking from 1 again for the next empty cell
					k = 1
					print(empty_list)
					print_sudoku(sudoku)
					break
				# incase none of the values from 1 to 9 fit the given cell
				# we need to back track to the last cell that had a value less than 9
				# and change that value to a newer value that satisfies the solution
				# while backtracking we also need to convert all the cells to 0 
				# such that it doesnt interfere with the solution. 
				else:
					while k >= 9:
						print('Value not found, backtracking')
						i,j = empty_list.pop()
						k = sudoku[i][j]
						sudoku[i][j] = 0
				k+=1
		j+=1
		# change the column if we are on last row
		# and go back to the first row.
		if j>8:
			i+=1
			j=0
		if i>8:
			break


if __name__ == "__main__":
	sudoku = create_sudoku()
	solve_sudoku(sudoku)

else:
	print("Run from main")