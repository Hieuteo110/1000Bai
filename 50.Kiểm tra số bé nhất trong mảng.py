n=int(input("Nhập số phần tử của mảng: "))
A=[]
for i in range(n):
    so=int(input(f"Nhập A[{i}]: "))
    A.append(so)
min=A[0]
for i in A:
    if i<=min:
        min=i
print(f"Số bé nhất trong mảng: {min}")
