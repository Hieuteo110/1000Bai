A=[]
n=int(input("Nhập số n: "))
for i in range(1,n+1):
    if n%i==0 and i%2!=0:
       A.append(i)
so=" ".join(str(i)for i in A)
print("Các ước lẻ:",so)