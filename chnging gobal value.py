#change global variable value
y=20
def change():
    global y
    y=40
    print(y)
change()
print(y)
