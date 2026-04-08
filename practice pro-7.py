#spy number:
n=int(input("Enter a number"))
sum_digits=0
product_digits=1
temp=n
while temp>0:
    digit=temp%10
    sum_digits+=digit
    product_digits*=digit
    temp=temp//10
if sum_digits==product_digits:
      print("spy number")
else:
      print("Not a spy number")
