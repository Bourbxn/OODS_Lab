'''
Into the Woods
'''

class Stack():
    def __init__(self, ls = None):
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
            val = self.stack.pop()
        return val

    def getStack(self):
        return self.stack

def tree_saw(stack,temp):
    maxH = 0
    saw = 0
    while not stack.isEmpty():
        if stack.peek() > maxH:
            maxH = stack.peek()
            saw += 1
        temp.push(stack.pop())

    while not temp.isEmpty():
        stack.push(temp.pop())
    print(saw)


if __name__ == '__main__':
    S = Stack()
    temp = Stack()
    inp = input('Enter Input : ').split(',')
    for i in inp:
        op = i.split()[0]
        if op == 'A':
            height = i.split()[1]
            S.push(int(height))
        elif op == 'B':
            tree_saw(S,temp)

#A 8,A 3,A 2,A 6,A 2,B,A 10,B
            