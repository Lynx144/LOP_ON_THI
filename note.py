soluong=int(input())
phong={}
for cuochop in range(1,soluong+1):
    a,b=map(int,input().split())
    phong={a:b}
print(phong)