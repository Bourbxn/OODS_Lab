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
    inp = input("Enter people : ")
    lst = [i for i in inp]
    queue = Queue()
    cashier1 = Queue()
    cashier2 = Queue()
    for i in lst:
        queue.enQueue(i)
    time = 0
    timec2 = 0
    while not queue.isEmpty():
        time+=1
        if cashier1.size()<5:
            val = queue.deQueue()
            cashier1.enQueue(val)
        else:
            timeDelta = time
            val = queue.deQueue()
            cashier2.enQueue(val)
        print("{} {} {} {}".format(time,queue,cashier1,cashier2))
        if time%3==0:
            cashier1.deQueue()
        if not cashier2.isEmpty():
            timec2+=1
            if timec2%2==0 and timec2>0:
                cashier2.deQueue()