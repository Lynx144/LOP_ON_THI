p,q,r=map(int,input().split())
if (p==q and p>r ) or (p==r and p>q) or (r ==q and r>p) or r==q==p:
    print("BAU LAI")
elif p>q and p > r:
    print("AN")
elif q>p and q>r:
    print("VINH")
else:
    print("QUANG")