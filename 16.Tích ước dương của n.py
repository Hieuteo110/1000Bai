s=1
n=int(input("Nhập số n:"))
for i in range(1,n+1):
    if n%i==0:
        s*=i
print("Tích:",s)