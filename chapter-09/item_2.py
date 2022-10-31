'''
Straight Selection Sort [recursive]
'''
def selection_sort(l: list, i: int = 0) -> list:
    if len(l)-1 == i:
        return
    max_i = l.index(max(l[:len(l)-i-1]))
    cur_i = len(l)-i-1
    if  max_i != cur_i:
        if l[max_i] > l[cur_i]:
            print(f"swap {l[cur_i]} <-> {l[max_i]} : ",end='')
            l[max_i], l[cur_i] = l[cur_i], l[max_i]
            print(l)
        selection_sort(l,i+1)
    return l

def main():
    print(selection_sort(list(map(int, input("Enter Input : ").split()))))

if __name__ == '__main__':
    main()
