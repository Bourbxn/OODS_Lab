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

if __name__ == '__main__':
    inp = input("Enter code,hint : ")
    code = inp.split(",")[0]
    hint = inp.split(",")[1]
    hintLs = [i for i in code]
    rot = ord(hint)-ord(code[0])
    queue = Queue()
    for i in hintLs:
        queue.enQueue(chr(ord(i)+rot))
        print(queue)