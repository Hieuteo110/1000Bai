n=int(input("Nhập số n: "))
j=n
check=True
while n>0:
    i=n%10
    if i%2==0:
        check=True
    else:
        check=False
        break
    n//=10
if check:
    print(j,"toàn số chẵn")
else:
    print(j,"có số lẻ")