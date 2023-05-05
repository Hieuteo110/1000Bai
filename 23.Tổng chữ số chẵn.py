n=int(input("Nhập số n: "))
s=0
while n>0:
    i=n%10
    if i%2==0:
        s+=i
    n//=10
print("Tổng số chẵn:",s)