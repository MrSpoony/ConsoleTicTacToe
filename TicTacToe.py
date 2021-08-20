def drawBoard():
	print("")
	print("")
	print("")
	for i in range(0, 8, 3):
		print(f"{board[i]} | {board[i+1]} | {board[i+2]}\n----------")
def isunused(turn):
	global board1, board
	if board[turn] ==  board1[turn]:
		return turn
	else:
		isunused(int(input(("You cannot place your turn there, Try again Please: "))))
def nextTurn():
	global XorO
	if XorO == "X":
		turn = int(input("Its Xs Turn, enter Number: "))
		board[isunused()] = XorO
	else:
		turn = int(input("Its Os Turn, enter Number: "))
		board[isunused()] = XorO
	drawBoard()
	if isWin():
		print(f"Game over! {XorO} won!")
		exit()
	else:
		if XorO == "X":
			XorO = "O"
		else:
			XorO = "X"
board, board1 = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
XorO = "X"
def isWin():
	whoseTurn = [XorO, XorO, XorO]
	if((board[0:3] == whoseTurn) or (board[3:6] == whoseTurn) or (board[6:9] == whoseTurn) or (board[0:7:3] == whoseTurn) or (board[1:8:3] == whoseTurn) or (board[2:9:3] == whoseTurn) or (board[0:9:4] == whoseTurn) or (board[2:7:2] == whoseTurn)):
		return True
	else:
		return False
drawBoard()
while True:
	nextTurn()