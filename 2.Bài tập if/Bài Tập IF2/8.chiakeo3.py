a,b,c=map(int,input().split())
res=min(a+b,a+c,b+c)
f_res=0
if res==a+b:
    f_res=res-c
if res==a+c:
    f_res=res-b
if res == b+c:
    f_res=res-a
print(abs(f_res))