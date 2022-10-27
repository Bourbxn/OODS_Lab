def minIndex( a , i , j ):
    if i == j:
        return i
    k = minIndex(a, i + 1, j)
    return (i if a[i] < a[k] else k)

def recurSelectionSort(a, n, index = 0):
    if index == n:
        return -1
    k = minIndex(a, index, n-1)
    if k != index:
        print(f"{a[k]} ? {a[index]}")
        a[k], a[index] = a[index], a[k]
    recurSelectionSort(a, n, index + 1)

def main():
    inp = list(map(int,input("Enter Input : ").split()))
    recurSelectionSort(inp,len(inp))
    print(inp)

if __name__ == '__main__':
    main()
