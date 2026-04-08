#VARIBLES
def display():
    a=10#local variable
    print("inside value is :",a)
display()
#print(a)(variable declared locally


#GLOBAL DECLARATION
x=10#global variable
def display():
    print("inside fun:",x)
display()
print("outside fun:",x)
