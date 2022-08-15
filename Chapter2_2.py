import math

class Spherical:

    def __init__(self,radius):
        self.radius = radius

    def changeR(self,newRadius):
        self.radius = newRadius

    def findVolume(self):
        return 4/3*math.pi*self.radius**3

    def findArea(self):
        return 4*math.pi*(self.radius**2)

    def __str__(self):
        return "Radius ={0} Volumn = {1} Area = {2}".format(self.radius,self.findVolume(),self.findArea())

r1, r2 = input("Enter R : ").split()
R1 = Spherical(int(r1))
print(type(R1))
print(dir(R1))
print(R1)
R1.changeR(int(r2))
print(R1)