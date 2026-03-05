n=int(input())
res=0
for i in range(1,len(str(n))+1):
    res+=n%10
    n//=10
print(res)