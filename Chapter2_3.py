def rangeFn(end,start=0,step=1):
	rangeList = []
	loop = int((end-start+1)/step)
	for i in range(loop):
		numToAdd = start+(step*i)
		if numToAdd<end:
			rangeList.append(float(numToAdd))
	for i in range(len(rangeList)):
		rangeList[i]=float("{:.3f}".format(rangeList[i]))
	return rangeList

def toTuple(list):
	return tuple(list)

if __name__ == '__main__':
	print("*** New Range ***")
	listNum = list(map(float,input("Enter Input : ").split()))
	llNum = len(listNum)
	if(llNum==1):
		print(toTuple(rangeFn(listNum[0])))
	elif(llNum==2):
		print(toTuple(rangeFn(listNum[1],listNum[0])))
	elif(llNum==3):
		print(toTuple(rangeFn(listNum[1],listNum[0],listNum[2])))

