'''
รู้จักกับ STACK
'''

class Stack:
	def __init__(self):
		self.stack = []

	def size(self):
		return len(self.stack)

	def isEmpty(self):
		if self.size()==0:
			return True
		else:
			return False

	def peek(self):
		if self.isEmpty():
			return None
		else:
			return self.stack[self.size()-1]

	def push(self, val):
		self.stack.append(val)

	def pop(self):
		if not self.isEmpty():
			self.stack.pop()

	def getStack(self):
		return self.stack
		
if __name__ == '__main__':
	stack = Stack()
	mesList = list(map(str,input("Enter Input : ").split(',')))
	for i in mesList:
		mes = i.split(" ")
		if mes[0]=='A':
			stack.push(mes[1])
			print("Add = {} and Size = {}".format(stack.peek(),stack.size()))
		elif mes[0]=='P':
			msg = "Pop = {} and Index = {}".format(stack.peek(),stack.size()-1)
			print("-1" if stack.isEmpty() else msg)
			stack.pop()
	print("Value in Stack = ",end="")
	if stack.isEmpty():
		print("Empty")
	else:
		print(*stack.getStack(),sep=" ")
	
