# n=int(input("Nhập số n: "))
# s=0
# for i in range(1,n):
#     if i%2!=0:
#         s+=i
#     i+=2
# print(f"Tổng các số lẻ bé hơn n: {s}")
n=int(input("Nhập số n: "))
i=1
s=0
while i<n:
    s+=i
    i+=2
print(f"Tổng các số lẻ bé hơn n: {s}")