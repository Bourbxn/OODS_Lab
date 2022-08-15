class TorKham:
	def __init__(self):
		self.wordList = []

	def p(self,word):
		if self.wordList==[]:
			self.wordList.append(word)
			return f"\'{word}\' -> {self.wordList}"
		else:
			if self.wordList[len(self.wordList)-1][-2].lower()+self.wordList[len(self.wordList)-1][-1].lower()==word[0].lower()+word[1].lower():
				self.wordList.append(word)
				return f'\'{word}\' -> {self.wordList}'
			else:
				return f'\'{word}\' -> game over'

	def r(self):
		self.wordList = []
		return 'game restarted'

if __name__ == '__main__':
	print("*** TorKham HanSaa ***")
	listWord = list(map(str,input("Enter Input : ").split(",")))
	torKham = TorKham()
	for i in listWord:
		nl = i.split()
		if nl[0] == 'P':
			print(torKham.p(nl[1]))
		elif nl[0] == 'R':
			print(torKham.r())
		elif nl[0] == 'X':
			break
		else:
			print(f'\'{i}\' is Invalid Input !!!')
			break

