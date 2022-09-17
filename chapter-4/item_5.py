'''
Color Crush 2
'''

class Queue():
    def __init__(self, ls = []):
        self.queue = []

    def size(self):
        return len(self.queue)

    def isEmpty(self):
        return True if self.size()==0 else False

    def enQueue(self, val):
        self.queue.append(val)

    def deQueue(self):
        return self.queue.pop(0)

    def __str__(self):
        return str(self.queue)

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

def isExplode(stack):
    temp = Stack()
    colorRound = 0
    isExplode = False
    for i in range(stack.size()):
        temp.push(stack.pop())
        if stack.peek()==temp.peek():
            colorRound += 1
            if colorRound == 2:
                isExplode = True
                break
        else:
            colorRound = 0
    while not temp.isEmpty():
        stack.push(temp.pop())
    return isExplode

def colorExplode(stack):
    temp = Stack()
    colorRound = 0
    colorExplode = None
    while not stack.isEmpty():
        temp.push(stack.pop())
        if stack.peek()==temp.peek():
            colorRound += 1
            if colorRound == 2:
                colorExplode = stack.pop()
                temp.pop()
                temp.pop()
                break
        else:
            colorRound = 0
    while not temp.isEmpty():
        stack.push(temp.pop())
    return colorExplode

def normalExplode(stack,explode):
    temp = Stack()
    colorRound = 0
    isExpdFail = [False,False]
    while not stack.isEmpty():
        temp.push(stack.pop())
        if stack.peek()==temp.peek():
            colorRound += 1
            if colorRound == 2 and explode.size()>0:
                item = explode.deQueue()
                if item == stack.peek():
                    isExpdFail[1] = True
                    stack.pop()
                    temp.pop()
                    temp.pop()
                    temp.push(item)
                    break
                else:
                    temp.push(item)
                    break
            elif colorRound == 2 and explode.size()==0:
                isExpdFail[0] = True
                stack.pop()
                temp.pop()
                temp.pop()
                break
        else:
            colorRound = 0
    while not temp.isEmpty():
        stack.push(temp.pop())
    return isExpdFail


def main():
    normal,mirror = input("Enter Input (Normal, Mirror) : ").split()
    normal = normal[::-1]
    explosives = 0
    failedIntrp = 0
    mrExplosives = 0
    mr = Stack()
    nm = Stack()
    explode = Queue()
    for i in mirror:
        mr.push(i)
    for i in normal:
        nm.push(i)
    while isExplode(mr):
        mrExplosives += 1
        explode.enQueue(colorExplode(mr))
    while isExplode(nm):
        expdFail = normalExplode(nm,explode)
        if expdFail[0]:
            explosives+=1
        if expdFail[1]:
            failedIntrp+=1
    print("NORMAL :")
    print(nm.size())
    print(*nm.getStack() if not nm.isEmpty() else "Empty",sep='')
    print(f'{explosives} Explosive(s) ! ! ! (NORMAL)')
    print(f'Failed Interrupted {failedIntrp} Bomb(s)\n' if failedIntrp>0 else '',end='')
    print("------------MIRROR------------")
    print(": RORRIM")
    print(mr.size())
    print(*mr.getStack() if not mr.isEmpty() else "ytpmE",sep='')
    print(f'(RORRIM) ! ! ! (s)evisolpxE {mrExplosives}')

if __name__ == '__main__':
    main()


