class Stack:
	def __init__(self):
		self.stack = []

	def size(self):
		return len(self.stack)

	def isEmpty(self):
		return True if self.size()==0 else False

	def peek(self):
		return None if self.isEmpty() else self.stack[self.size()-1]

	def push(self, val):
		self.stack.append(val)

	def pop(self):
		if not self.isEmpty():
			self.stack.pop()

	def getStack(self):
		return self.stack

def Add(stack,number):
	stack.push(number)
	print("Add = {}".format(number))

def Pop(stack):
	if stack.isEmpty():
		print('-1')
	else:
		print("Pop = {}".format(stack.peek()))
		stack.pop()	

def Delete(stack,temp,number):
	while not stack.isEmpty():
		if stack.peek()==number:
			print("Delete = {}".format(stack.peek()))
			stack.pop()
		else:
			temp.push(stack.peek())
			stack.pop()
	while not temp.isEmpty():
		stack.push(temp.peek())
		temp.pop()

def LessDelete(stack,temp,number):
	while not stack.isEmpty():
		if stack.peek()<number:
			print("Delete = {} Because {} is less than {}".format(stack.peek(),stack.peek(),number))
			stack.pop()
		else:
			temp.push(stack.peek())
			stack.pop()	
	while not temp.isEmpty():
		stack.push(temp.peek())
		temp.pop()
	

def MoreDelete(stack,temp,number):
	while not stack.isEmpty():
		if stack.peek()>number:
			print("Delete = {} Because {} is more than {}".format(stack.peek(),stack.peek(),number))
			stack.pop()
		else:
			temp.push(stack.peek())
			stack.pop()	
	while not temp.isEmpty():
		stack.push(temp.peek())
		temp.pop()

def ManageStack(act,stack,temp,number=None):
	if act == "A":
		Add(stack,number)
	elif act == "P":
		Pop(stack)
	elif act == "D":
		if not stack.isEmpty():
			Delete(stack,temp,number)
		else:
			print(-1)
	elif act == "LD":
		if not stack.isEmpty():
			LessDelete(stack,temp,number)
		else:
			print(-1)
	elif act == "MD":
		if not stack.isEmpty():
			MoreDelete(stack,temp,number)
		else:
			print(-1)

if __name__ == '__main__':
	stack = Stack()
	temp = Stack()
	mesList = list(map(str,input("Enter Input : ").split(',')))
	for i in mesList:
		actList = i.split()
		if len(actList)==1:
			ManageStack(actList[0],stack,temp)
		else:
			ManageStack(actList[0],stack,temp,int(actList[1]))
	print("Value in Stack =",stack.getStack())

