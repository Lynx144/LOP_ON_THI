a=int(input())
b=int(input())
c=int(input())

i=((a+b+c)/(a*b*c))+(a*b*c)**0.5
A=i%0.01
i=i-A

print(i)