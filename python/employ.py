class Employee:
    def __init__(self,a,b,c,d):
        self.code=a
        self.name=b
        self.age=c
        self.salary=d
    def printdata(self):
        print("code=",self.code)
        print("name=",self.name)
        print("age=",self.age)
        print("salary=",self.salary)

s=Employee("a12","arjun",12,5000)
s1=Employee("a13","sibin",14,1000)
s2=Employee("a14","shyam",16,20000)
s3=Employee("a16","aju",17,2500)
s.printdata()
s1.printdata()
s2.printdata()
s3.printdata()