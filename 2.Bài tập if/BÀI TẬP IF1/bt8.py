import random
a=random.randint(0,1)
b=random.randint(0,1)
c=random.randint(0,1)
if a!= b and a!=c:
    print("1")
elif b!=a and b!=c:
    print("2")
elif c!=a and c!= b:
    print("3")