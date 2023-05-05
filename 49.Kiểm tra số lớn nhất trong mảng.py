n=int(input("Nhập số phần tử của mảng: "))
A=[]
for i in range(n):
    so=int(input(f"Nhập A[{i}]: "))
    A.append(so)
max=A[0]
for i in A:
    if i>=max:
        max=i
print(f"Số lớn nhất trong mảng: {max}")
