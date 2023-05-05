n=int(input("Nhập số n: "))
s=0
while n>0:
    if (n%10)%2!=0:
        s+=1
    n//=10
print("Có",s," chữ số lẻ")