print("Nhập số từ 1-32000")
n=int(input())
m=int(input("Nhập số nguyên thứ 2:"))
if not 1<=(n and m)<=32000:
    print("Số không hợp lệ")
    print("Vui lòng nhập lại số từ 1-32000")
    breakpoint
else:
    print(f"{n} + {m} = {n+m}")
    print(f"{n} - {m} = {n-m}")
    print(f"{n} * {m} = {n*m}")
    print(f"{n} div {m} = {n//m}")