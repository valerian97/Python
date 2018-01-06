#Tic Tac Toe

class game:
	pos = [[' ' for i in range(3)] for j in range(3)]
	won = -1
	def hasWon(self):
		exp3 = self.pos[0][0] == self.pos[1][1] == self.pos[2][2] and self.pos[1][1] != ' '
		exp4 = self.pos[1][1] == self.pos[0][2] == self.pos[2][0] and self.pos[1][1] != ' '
		for i in range(3):
			exp1 = self.pos[i][0] == self.pos[i][1] == self.pos[i][2] and self.pos[i][0] != ' '
			exp2 = self.pos[0][i] == self.pos[1][i] == self.pos[2][1] and self.pos[0][i] != ' '
			check1 = self.pos[i][0]
			check2 = self.pos[0][i]
			exp = [exp1, exp2]
			check = [check1, check2]
			for i in range(2):
				if(exp[i]):
					if(check[i] == '0'):
						self.won = 1
					else:
						self.won = 2
		if(exp3 or exp4):
			if(self.pos[1][1] == '0'):
				self.won = 1
			else:
				self.won = 2
	def disp(self):
		print('')
		print(' '*8+ 'B O A R D' + ' '*8)
		for i in range(3):
			print('+-------'*3 + '+')
			print('|       '*3 + '|')
			strs = ['|   ' + str(self.pos[i][j]) + '   ' for j in range(3)]
			print(''.join(strs) + '|')
			print('|       '*3 + '|')
		print('+-------'*3 + '+')
		if(self.won == 1):
			print('\nCongratulations: Player 1 (i.e: 0) has won')
		elif(self.won == 2):
			print('\nCongratulations: Player 2 (i.e: X) has won')
	def place(self, player):
		while(True):
			try:
				posX = int(input('Enter x pos of point: '))
				posY = int(input('Enter y pos of point: '))
				assert posX >= 1 #Make sure no data is indexed as -1, throws exception if so.
				assert posY >= 1 
				if self.pos[posY-1][posX-1] != ' ':
					print('This position is already taken!')
					raise Exception("taken")
				if player == 0:
					self.pos[posY-1][posX-1] = '0' 
				else:
					self.pos[posY-1][posX-1] = 'X'
			except Exception as error:
				print('Invalid input, try again')
			else:
				break
	def handler(self):
		print('Welcome to X and O. Player 1, place your first 0')
		while(self.won == -1):
			for i in range(2):
				self.place(i)
				self.hasWon()
				self.disp()
				if(self.won != -1):
					break;
Game = game()
Game.handler()

