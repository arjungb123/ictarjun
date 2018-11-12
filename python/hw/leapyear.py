n=int(input("enter the  year"))
if(n%4==0):
    print("leapyear")
elif(n%400==0):
    print("palindrome")
else:
    print("not palinfrome")