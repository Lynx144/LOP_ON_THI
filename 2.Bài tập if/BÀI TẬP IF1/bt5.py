x,y,z=input().split()
x=int(x)
y=int(y)
z=int(z)
if x==y!=z or x!=y==z or x==z!=y:
    print('YES')
else:
    print('NO')