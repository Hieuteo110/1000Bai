x = int(input("Nhập số x: "))
n = int(input("Nhập số n: "))
s = 0
for k in range(1, n+1):
    s += (-1)**(k+1) * (x**k)
print(s)