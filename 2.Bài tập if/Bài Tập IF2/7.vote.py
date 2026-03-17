a,b,c=map(int,input().split())
if max(a,b,c)>c:
    print(max(a,b,c,)-c+1)
elif max(a,b)==c:
    print(1)

else:
    print(max(a,b,c)-c)