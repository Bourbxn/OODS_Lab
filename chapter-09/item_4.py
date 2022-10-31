'''
Find the Running Median
'''
def bubble_sort(l: list) -> list:
    if len(l) <= 1:
        return l
    if len(l) == 2:
        return l if l[0] < l[1] else [l[1], l[0]]
    a, b = l[0], l[1]
    bs = l[2:]
    r = []
    if a < b:
        r = [a] + bubble_sort([b] + bs)
    else:
        r = [b] + bubble_sort([a] + bs)
    return bubble_sort(r[:-1]) + r[-1:]

def median(l: list) -> float:
    l = bubble_sort(l)
    idx = int(len(l)/2)
    if len(l)%2!=0:
        return l[idx]
    return (l[idx]+l[idx-1])/2

def run_list(l: list) -> None:
    for i in range(1,len(l)+1):
        print(f"list = {l[:i]} : median = {median(l[:i]):.1f}")

l = [e for e in input("Enter Input : ").split()]
if l[0] == 'EX':
    Ans = "bubble sort"
    print("Extra Question : What is a suitable sort algorithm?")
    print("   Your Answer : "+Ans)
else:
    l=list(map(int, l))
    run_list(l)
    
