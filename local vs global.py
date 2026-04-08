#local vs global variables
x=100
def display():
    x=10
    print("the value for inside:",x)
display()
print("the value for outside:",x)
