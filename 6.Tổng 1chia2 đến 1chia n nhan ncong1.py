s=0
n=int(input("Nhập số n: "))
for i in range(1,n+1):
    s=s+1.0/(i*(i+1))
print(s)