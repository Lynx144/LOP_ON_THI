p1,p2,p3=input().split()
p1=int(p1)
p2=int(p2)
p3=int(p3)
if p1 == p2 ==p3:
    print(3)
elif p1==p2 or p1== p3 or p3==p2:
    print(2)
else:print(1)