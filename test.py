def checkOddEven(number):
    if number%2==0:
        return "even"
    else:
        return "odd"

print(" *** 3-digit odd even ***")
number = input("Enter 3-digit number : ")
a = int(number[0])
b = int(number[1])
c = int(number[2])
oa = checkOddEven(a)
ob = checkOddEven(b)
oc = checkOddEven(c)
print(f'{number} => {oa} {ob} {oc}')


