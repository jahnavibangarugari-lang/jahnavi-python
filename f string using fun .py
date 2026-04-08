#display of name and age using f string and functions
def display():
    name="janu"
    age=19
    print(f'my name is {name} and I am {age} years old')
display()
#without f string
def display():
    name="janu"
    age=19
    print(name,age,sep="\n")
display()
def display(
    name="janu",
    age=19):
    print(f'my name is {name} and I am {age} years old')
display("ram",20)
display(18,"hasini")
