#top-down approach

#ADDITION OF TWO NUMBERS
def add(a,b):#formal argument/parameter 
    return a+b
x=int(input("enter x value"))
y=int(input("enter y value"))
result=add(x,y)#actual argument
print(result)

#AREA OF RECTANGLE
def main():
    l,b=get_values()
    area=calculate_area(l,b)
    display(area)
def get_values():
    return 5,3
def calculate_area(l,b):
    return l*b
def display(area):
    print("AREA IS:",area)
main()
