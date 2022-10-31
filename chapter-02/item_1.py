'''
Simple OOP Calculator
'''
class Calculator :

    def __init__(self,var):
        self.var = var

    def __add__(self,otherVar):
        return self.var+otherVar.var

    def __sub__(self,otherVar):
        return self.var-otherVar.var

    def __mul__(self,otherVar):
        return self.var*otherVar.var

    def __truediv__(self,otherVar):
        return self.var/otherVar.var

x,y = input("Enter num1 num2 : ").split(",")

x,y = Calculator(int(x)),Calculator(int(y))

print(x+y,x-y,x*y,x/y,sep = "\n")