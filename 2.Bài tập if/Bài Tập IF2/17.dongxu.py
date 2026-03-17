n=int(input())
xu1=n//3
xu2=xu1
tong=n-(xu1+xu2*2)
if tong ==0:
    print(f"{xu1} {xu2}")
elif tong>0:
    xu1+=tong%2
    xu2+=tong//2
    print(f"{xu1} {xu2}")