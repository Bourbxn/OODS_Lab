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

def postFixeval(st):
    stack = Stack()
    for i in st:    
        try:
            stack.push(float(i))
        except ValueError:
            val1 = stack.pop()
            val2 = stack.pop()
            if i == '/':
                stack.push(val2 / val1)
            else:       
                switcher ={'+':val2 + val1, '-':val2-val1, '*':val2 * val1, '^':val2**val1}
                stack.push(switcher.get(i))
    return float(stack.pop())

if __name__ == '__main__':
    print(" ***Postfix expression calcuation***")
    token = list(input("Enter Postfix expression : ").split())

    print("Answer : ",'{:.2f}'.format(postFixeval(token)))