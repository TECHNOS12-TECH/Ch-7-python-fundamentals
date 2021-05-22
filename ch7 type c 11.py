# To calculate Simple Interest and Compound Interest
p=float(input("Enter Principal value:"))
r=float(input("Enter value of Rate:"))
t=float(input("Enter time of interest:"))
SI=p*r*t/100
CI= p*((1+(r/100))**t)-p
print("The Simple Interest is:",SI)
print("The Compound Interest is:",CI)
