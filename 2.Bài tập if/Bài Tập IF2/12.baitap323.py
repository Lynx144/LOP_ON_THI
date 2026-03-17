p,q,r,s,u,v = map(int, input().split())
A = B = C = 0

if p > q:
    A += 3
elif p < q:
    B += 3
else:
    A += 1
    B += 1

if r > s:
    A += 3
elif r < s:
    C += 3
else:
    A += 1
    C += 1

if u > v:
    B += 3
elif u < v:
    C += 3
else:
    B += 1
    C += 1

print(f"{A} {B} {C}")