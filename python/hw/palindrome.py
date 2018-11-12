def pal(n):
    rev=0
    while(n>0):
        r=n%10
        rev=(rev*10)+r
        n=n//10
    if(n==rev):
        print("palindrome")
    else:
        print(" not palindrome")
x=int(input("enter numbr"))
pal(x)
