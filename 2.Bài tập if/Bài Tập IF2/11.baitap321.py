import math
x,y,u,v=map(int,input().split())
w=abs(x-u)
l=abs(y-v)
if w==l:
    res=(w/2)**2 *math.pi
    print('HINH VUONG')
    print(f'{res:.4f}')
else:
    res=((w/2)**2 + (l/2)**2) * math.pi
    print('HINH CHU NHAT')
    print(f'{res:.4f}')