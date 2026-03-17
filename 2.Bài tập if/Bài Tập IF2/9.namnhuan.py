n=int(input())
if (n%3328==0):
    print("Multi leap")
elif (n % 4 ==0 and not n%100==0) or (n%400==0):
    print("Leap")
else:
    print("No")