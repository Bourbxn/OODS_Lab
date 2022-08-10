def most_frequent(List):
    return max(set(List), key = List.count)

def checkAllError(list):
	error = 0
	for i in list:
		if i < 1 or i > 20:
			error+=1
			break
	if(error==len(list)):
		return True
	else:
		return False

def clearAllMinus(list):
	numberToRemove=[]
	for i in range(len(list)):
		if list[i]<1 or list[i]>20:
			numberToRemove.append(list[i])
	for i in numberToRemove:
		list.remove(i)
	return list
    

print("*** Election ***")
num = int(input("Enter a number of voter(s) : "))
listNum = list(map(int,input().split()))
listNumRemove = clearAllMinus(listNum)

if(checkAllError(listNum)):
	print("*** No Candidate Wins ***")
else:
	print(most_frequent(listNumRemove))
