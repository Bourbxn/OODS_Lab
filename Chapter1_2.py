listNum = list(map(float,input("Enter your High and Weight : ").split()))
bmi = listNum[1]/(listNum[0]**2)
if(bmi<18.5):
	print("Less Weight")
elif(bmi>=18.5 and bmi<23.0):
	print("Normal Weight")
elif(bmi>=23.0 and bmi<25.0):
	print("More than Normal Weight")
elif(bmi>=25.0 and bmi<30.0):
	print("Getting Fat")
else:
	print("Fat")