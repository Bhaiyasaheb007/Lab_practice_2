
			


def solveNQueens(n):
	ans = []
	board = [['.'] * n] * n
	#print(board)
	lowerDiagonal = [0] * (2*n-1)
	upperDiagonal = [0] * (2*n-1)
	leftRow = [0] * n
	
	def solve( col, board, ans, leftRow, lowerDiagonal, upperDiagonal, n):
		if(col == n):
			copy = ["".join(row) for row in board]
			ans.append(copy)
			return
		
		for row in range(n):
			if leftRow[row] == 0 and lowerDiagonal[row+col] == 0 and upperDiagonal[n-1 + col - row] == 0:
				board[row][col]= 'Q'
				leftRow[row] = 1
				lowerDiagonal[row+col] = 1
				upperDiagonal[n-1 + col - row] = 1
				solve(col+1, board, ans, leftRow, lowerDiagonal, upperDiagonal, n)
				board[row][col] = '.'
				leftRow[row] = 0
				lowerDiagonal[row+col] = 0
				upperDiagonal[n-1 + col - row] = 0
			
	solve(0, board, ans, leftRow, lowerDiagonal, upperDiagonal, n)
	return ans
	
ans = solveNQueens(4)

for board in ans:
	for col in board:
		print(col)
	print("--------------------------------------------")
	
