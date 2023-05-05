n=int(input("Nhập số n: "))
s=0
max=n%10
while n>0:
    i=n%10
    if i>max:
        max=i
    n//=10
print("Số lớn nhất:",max)