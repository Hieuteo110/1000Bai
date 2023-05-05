n=int(input("Nhập số n: "))
min=n%10
while n>0:
    i=n%10
    if i<min:
        min=i
    n//=10
print("Số nhỏ nhất:",min)