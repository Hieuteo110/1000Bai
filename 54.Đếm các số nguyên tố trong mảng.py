def nt(n):
    if n<2:
        return False
    else:
        for i in range(2,n):
            if n%i==0:
                return False
                break
        return True
n = int(input("Nhập số phần tử của mảng: "))
A = []
dem=0
for i in range(n):
    so = int(input(f"Nhập A[{i}]: "))
    A.append(so)
for i in A:
    if nt(i):
        dem+=1
print(f"Đếm các số nguyên tố trong mảng: {dem}")