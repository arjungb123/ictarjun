def re(a):
    n=a
    rev=0
    while(n>0):
      r=n%10
      rev=(rev*10)+r
      n=n//10
    return rev
x=int(input("enter the number"))        
print("reverse",re(x))