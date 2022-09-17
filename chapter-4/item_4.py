'''
เดาใจไว้แล้วว่าเธอรักฉันแบบที่ฉันรัก
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

def calculate_score(valMy,valYour):
    scoreAdd = 0
    if valMy[0]==valYour[0] and valMy[-1]!=valYour[-1]:
        scoreAdd += 1
    elif valMy[0]!=valYour[0] and valMy[-1]==valYour[-1]:
        scoreAdd += 2
    elif valMy[0]==valYour[0] and valMy[-1]==valYour[-1]:
        scoreAdd += 4
    else:
        scoreAdd -= 5
    return scoreAdd

def display_key(size,queue):
    for i in range(size):
        val = queue.deQueue()
        queue.enQueue("{}:{}".format(action.get(val[0]),place.get(val[-1])))
        print(val if i==size-1 else val+', ' ,end = '')
    print()

def display_mes(size,queue):
    for i in range(size):
        val = queue.deQueue()
        print(val if i==size-1 else val+', ' ,end = '')
    print()

if __name__ == '__main__':
    action = {
        "0":"Eat",
        "1":"Game",
        "2":"Learn",
        "3":"Movie"
    }
    place = {
        "0":"Res.",
        "1":"ClassR.",
        "2":"SuperM.",
        "3":"Home"
    }
    score = 0
    meyou = input("Enter Input : ").split(',')
    myQ = Queue()
    yourQ = Queue()
    for i in meyou:
        myQ.enQueue(i.split()[0])
        yourQ.enQueue(i.split()[1])
    qsize = myQ.size()
    for i in range(qsize):
        valMy = myQ.deQueue()
        myQ.enQueue(valMy)
        valYour = yourQ.deQueue()
        yourQ.enQueue(valYour)
        score += calculate_score(valMy,valYour)
    print("My   Queue = ",end='')
    display_key(qsize,myQ)
    print("Your Queue = ",end='')
    display_key(qsize,yourQ)
    print("My   Activity:Location = ",end='')
    display_mes(qsize,myQ)
    print("Your Activity:Location = ",end='')
    display_mes(qsize,yourQ)
    if score>=7:
        print("Yes! You're my love! : Score is {}.".format(score))
    elif score>0:
        print("Umm.. It's complicated relationship! : Score is {}.".format(score))
    else:
        print("No! We're just friends. : Score is {}.".format(score))
