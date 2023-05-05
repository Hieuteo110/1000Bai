n = int(input("Nhập số phần tử của mảng: "))
A = []
for i in range(n):
    so = int(input(f"Nhập A[{i}]: "))
    A.append(so)
min = A[0]
index_min = 0
for i in range(len(A)):
    if A[i] <= min:
        min = A[i]
        index_min = i
print(f"Vị trí số bé nhất trong mảng là A[{index_min}]: {A[index_min]}")