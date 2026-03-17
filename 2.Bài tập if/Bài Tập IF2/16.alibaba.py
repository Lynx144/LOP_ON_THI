a, b = map(int,input().split())
res= 3*a+b
vang=res
bac= vang+b
dong=bac+b
if vang<=0 or vang+bac+dong!=a:
    print(-1)
else:
    print(f"{vang} {bac} {dong}")
