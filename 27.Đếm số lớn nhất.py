n = int(input("Nhập số n: "))
max = n%10
A=[]
s = 0
if n>=10:
    while n > 0:
        i=n%10
        A.append(i)
        if i>max:
            max=i
        n//=10
    for i in A:
        if i==max:
            s+=1
else:
    s=1       
print("Số lớn nhất của n là:", max)
print("Số lần xuất hiện của số lớn nhất là:", s)