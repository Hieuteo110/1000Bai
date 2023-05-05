n=int(input("Nhập số n: "))
i=1
A=[]
while i<n:
    A.append(str(i))
    i+=2
s=" ".join(A)
print(f"Các số lẻ bé hơn n: {s}")