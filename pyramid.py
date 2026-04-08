
n = int(input("Enter number of rows: "))

for i in range(1, n + 1):
    
    # Print spaces
    for j in range(n - i):
        print(" ", end="")
    
    # Print increasing numbers
    for k in range(1, i + 1):
        print(k, end="")
    
    # Print decreasing numbers
    for l in range(i - 1, 0, -1):
        print(l, end="")
    
    print()
