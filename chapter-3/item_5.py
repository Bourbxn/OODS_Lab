'''
ซอยตัน
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

def arrive(stack,temp,m,n):
    if stack.size()==m:
        print("car {} cannot arrive : Soi Full".format(n))
    else:
        addCar = False
        while not stack.isEmpty():
            if stack.peek() == n:
                print("car {} already in soi".format(n))
                break
            else:
                temp.push(stack.pop())
        if stack.isEmpty():
            addCar = True
            print("car {} arrive! : Add Car {}".format(n,n))
        while not temp.isEmpty():
            stack.push(temp.pop())
        if addCar:
            stack.push(n)
    print(stack.getStack())

def depart(stack,temp,m,n):
    if stack.size()==0:
        print("car {} cannot depart : Soi Empty".format(n))
    else:
        wasRemove = False
        while not stack.isEmpty():
            if stack.peek()==n:
                wasRemove = True
                stack.pop()
                print("car {} depart ! : Car {} was remove".format(n,n))
                break
            else:
                temp.push(stack.pop())
        if not wasRemove:
            print("car {} cannot depart : Dont Have Car {}".format(n,n))
        while not temp.isEmpty():
            stack.push(temp.pop())
    print(stack.getStack())


if __name__ == '__main__':
    print("******** Parking Lot ********")
    m,s,o,n = input("Enter max of car,car in soi,operation : ").split()
    m,n = int(m),int(n)
    parkLot = s.split(',')
    stack = Stack()
    temp = Stack()
    for i in parkLot:
        if int(i)!=0:
            stack.push(int(i))
    if o == 'arrive':
        arrive(stack,temp,m,n)
    elif o == 'depart':
        depart(stack,temp,m,n)
