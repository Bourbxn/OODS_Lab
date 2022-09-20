'''
Perket
'''
def comb(l, n):
    if n == 0:
        return [[]]
    ls =[]
    for i in range(len(l)):         
        m = l[i]
        rmls = l[i + 1:]
        rmlscb = comb(rmls, n-1)
        for p in rmlscb:
             ls.append([m, *p])     
    return ls

def sb_cal(l):
    s,b = 1,0 
    for i in l:
        s*=int(i.split()[0])
        b+=int(i.split()[1])
    return abs(s-b)

def perket_cal(l,n,m):
    min = int(m)
    if n>0:
        for i in comb(l,n):
            nmin = sb_cal(i)
            min = nmin if nmin<min else min
        return perket_cal(l,n-1,min)
    return m

def main():
    l = input("Enter Input : ").split(',')
    print(perket_cal(l,len(l),10e9))

if __name__ == '__main__':
    main()
