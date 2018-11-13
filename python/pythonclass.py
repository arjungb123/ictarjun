class Students:
    # name="mahesh"
    # rollno=2
    def __init__(self,x,y):
        self.name=x
        self.rollno=y
    def printdata(self):
        print("name="+str(self.name))
        print("rollno="+str(self.rollno))


    def getage(self,myage):
        print("age is ",myage)
s=Students("rahul",12)
x=int(input("enter the age"))
s.getage(x)
s.printdata()