#palindrom or not:
n=int(input("Enter a string"))
temp=n
rev=0
while temp>0:
    digit=temp%10
    rev=rev*10+digit
    temp=temp//10
if rev==n:
   print("Palindrom Number")
else:
    print("Not a palindrom number")   
