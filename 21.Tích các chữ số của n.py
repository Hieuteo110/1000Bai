n=int(input("Nhập số n: "))
s=1
while n>0:
    s*=n%10
    n//=10
print("Tích chữ số:",s)