n=int(input("nhập số n: "))
def t(n):
    s=0
    for i in range(1,n+1):
        s+=i**3
    return s
print(f"Tổng = {t(n)}")