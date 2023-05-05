s=0
n=int(input("Nhập số n: "))
for i in range(1,n+1):
    if n%i==0 and i%2==0:
        s+=i
print("Tổng:",s)