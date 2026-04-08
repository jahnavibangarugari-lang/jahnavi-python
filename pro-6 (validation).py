#type vaidation
age=input("enter age")
if age.isdigit():
       age=int(age)
       print("valid age")
else:
    print("invalid age")


#range validation
n=int(input("enter a number"))
if 1<n<10:
       age=int(age)
       print("valid")
else:
    print("invalid")


#length validation
p=input("enter password")
if len(p)>=6:
    print("strong")
else:
    print("too weak")


#format validation
email=input("enter email")
if '@'in email and'.'in email:
    print("valid mail")
else:
    print("invalid mail")
    
