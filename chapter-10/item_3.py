'''
Fun with hashing
'''
class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "({0}, {1})".format(self.key, self.value)

class Hash:
    def __init__(self, t_size, max_coll):
        self.t_size = t_size
        self.max_coll = max_coll
        self.table = [None for i in range(t_size)]

    def full(self) -> None:
        if not None in self.table:
            print("This table is full !!!!!!")
            exit()

    def insert(self, key: str, val: str) -> None:
        self.full()
        coll = 0
        b_idx = idx = sum(ord(i) for i in key)%self.t_size
        while self.table[idx]:
            coll+=1
            print(f"collision number {coll} at {idx}")
            if coll == self.max_coll:
                print("Max of collisionChain")
                break
            idx = (b_idx+(coll**2))%self.t_size
        if not self.table[idx]:
            self.table[idx] = Data(key,val)

    def __str__(self):
        s = str()
        for i,val in enumerate(self.table):
            s += f"#{i+1}	{val}\n"
        return s + "---------------------------"

def main():
    print(" ***** Fun with hashing *****")
    inp = input("Enter Input : ").split('/')
    t_size, max_coll = int(inp[0].split()[0]),int(inp[0].split()[1])
    hash = Hash(t_size,max_coll)
    for i in inp[1].split(','):
        key, val = i.split()
        hash.insert(key,val) or print(hash)

if __name__ == '__main__':
    main()