'''
3 SUM(2)
'''

def n_length_combo(lst, n):
    if n == 0:
        return [[]]
    l =[]
    for i in range(0, len(lst)):         
        m = lst[i]
        remLst = lst[i + 1:]
        remainlst_combo = n_length_combo(remLst, n-1)
        for p in remainlst_combo:
             l.append([m, *p])     
    return l

def check_sum(lst):
    l =[]
    for i in range(len(lst)):
        if lst[i][0]+lst[i][1]+lst[i][2]==5:
            l.append(lst[i])
    rl = [i for n, i in enumerate(l) if i not in l[:n]] 
    return rl


if __name__=="__main__":
    numList = list(map(int,input("Enter Your List : ").split()))
    numList.sort()
    if len(numList)<3:
        print("Array Input Length Must More Than 2")
    else:
        print(check_sum(n_length_combo(numList, 3)))
