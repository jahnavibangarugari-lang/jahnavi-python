#default arguments
def sum(x=10,y=30,z=20):
    add=x+y+z
    print(add)
sum(x=10,y=90,z=20)
sum(x=10)
#requirement arguments
def sum(a,b):
    c=a+b
    print(c)
sum(10,20)
   #sum(30,40,50)# occurs error
#keyword arguments
def sum(x,y=30,z=40):
    addition=x+y+z
    print(addition)
sum(10,50,100)
sum(90)
 #keyword ex-2   
#def sum(x=30,y=20,z):#won't accept default value
    #addition=x+y+z
    #print(addition)
#sum(10,50,100)
#sum(90)
#variable-length arguments
def display(*no):#produce error without "*" symbol
    print(no)
display(10,20,30)
#poitionl arguments
def greet(name="janu",age=20):
    print(f'my name is {name} and i am {age} years old')
greet("janu",24)
greet(24,"janu")
