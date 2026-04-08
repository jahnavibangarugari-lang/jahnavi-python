#compound interest:
p=float(input("Enter principal amount: "))
r=float(input("Enter rate of interet: "))
t=float(input("Enter time(in years): "))
amount=p*(1+r/100)**t
ci=amount-p
print("Total amount=",amount)
print("compound interest=",ci)
