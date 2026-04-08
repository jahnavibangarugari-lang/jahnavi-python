n=int(input("enter a number: "))
temp=n
sum=0
digit=len(str(n))
while temp>0:
    r=temp%10
    sum=sum+(r**digit)
    temp=temp//10
if sum==n:
    print("Amstrong Number")
else:
    print("Not an Amstrong Number")
