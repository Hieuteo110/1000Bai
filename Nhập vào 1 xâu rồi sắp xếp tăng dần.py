n = input("Nhập dãy số nguyên: ")
A = n.split()
for i in range(1, len(A)):
    j = i - 1
    while j >= 0 and int(A[j]) > int(A[j+1]):
        A[j], A[j+1] = A[j+1], A[j]
        j -= 1
print(A)