print("*** Rabbit & Turtle ***")
listNum = list(map(float,input("Enter Input : ").split()))
d = listNum[0]
vt = listNum[1]
vr = listNum[2]
vf = listNum[3]
t = d/(vr-vt)
s = vf*t
print("%.2f"%s)