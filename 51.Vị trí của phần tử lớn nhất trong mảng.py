n=int(input("Nhập số phần tử của mảng: "))
A=[]
for i in range(n):
    so=int(input(f"Nhập A[{i}]: "))
    A.append(so)
max=A[0]
index_max=0
for i in range(len(A)):
    if A[i]>=max:
        max=A[i]
        index_max=i
print(f"Vị trí số lớn nhất trong mảng là A[{index_max}]: {A[index_max]}")
