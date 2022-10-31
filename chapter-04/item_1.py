'''
Basic Queue
'''

class Queue():
    def __init__(self, ls = None):
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
    inp = list(map(str,input("Enter Input : ").split(",")))
    queue = Queue()
    for i in inp:
        key = i.split()[0]
        if key=='E':
            num = i.split()[1]
            queue.enQueue(num)
            print("Add {} index is {}".format(num,queue.size()-1))
        elif key=='D':
            if not queue.isEmpty():
                val = queue.deQueue()
                print("Pop {} size in queue is {}".format(val,queue.size()))
            else:
                print("-1")
    if queue.isEmpty():
        print("Empty")
    else:
        print("Number in Queue is : ",queue)
