x=int(input("Nhập số x: "))
n=int(input("Nhập số n: "))
s=0
for i in range(1,n+1):
    p=x**(2*i-1)
    s+=p
print(s)