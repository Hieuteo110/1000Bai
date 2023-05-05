def twosum(A,n):
    for i in range(len (A)-1):
        for j in range(i+1,len(A)):
            if int(A[i])+int(A[j])==n:
                return [i,j]
    return []
x=input("Nhập vào mảng: ")
A=x.split()
n=int(input("Target= "))
print(twosum(A,n))