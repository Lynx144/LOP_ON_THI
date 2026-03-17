a,b=input().split()
a=float(a)
b=float(b)
if a ==0:
    if b==0:
        print("VSN")
    else:
        print("VN")
else:
    print(int(-b/a))