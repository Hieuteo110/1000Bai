n=int(input("Nhập số n: "))
A=[]
s=0
min=n%10
if n>=10:
    while n>0:
        i=n%10
        A.append(i)
        if i<min:
            min=i
        n//=10
    for i in A:
        if i==min:
            s+=1
else:
    s=1
print("Số nhỏ nhất:",min)
print("Số lần xuất hiện:",s)