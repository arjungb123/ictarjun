def largest(a,b,c):
    if(a>b and a>c):
        print("largest is",a)
    elif(b>c):
         print("largest is",b)
    else:
        print("largest is",c)

x=int(input("enter  number"))
y=int(input("enter number"))
z=int(input("enter number"))
largest(x,y,z)

