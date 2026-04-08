def fibnoci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibnoci(n-1)+fibnoci(n-2)
print(fibnoci(n))
