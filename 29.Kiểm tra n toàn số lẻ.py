n=int(input("Nhập số n: "))
j=n
check=True
while n>0:
    i=n%10
    if i%2==0:
        check=True
        break
    else:
        check=False
    n//=10
if check:
    print(j,"có số chẵn")
else:
    print(j,"toàn số lẻ")