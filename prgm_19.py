class rectangle():
    length=None
    width=None
    def __init__(self):
        self.length=int(input("Enter the length:"))
        self.width=int(input("enter your width:"))
    def area(self):
        return(self.length*self.width)
    
r1=rectangle()
r2=rectangle()
print("Area of Rectangle=",r1.area())
print("Area of Rectangle=",r2.area())
if r1.area()<r2.area():
    print("area2 is greater")
else:
    print("area1 is greater")
