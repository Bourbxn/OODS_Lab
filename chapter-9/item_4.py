def bubble_sort(l):
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

l = [e for e in input("Enter Input : ").split()]
if l[0] == 'EX':
    Ans = "xxx"
    print("Extra Question : What is a suitable sort algorithm?")
    print("   Your Answer : "+Ans)
else:
    l=list(map(int, l))

