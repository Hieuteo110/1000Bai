def UCLN(m, n):
    if n == 0:
        return m
    else:
        return UCLN(n, m % n)
def BCNN(m, n):
    return (m * n) // UCLN(m, n)
m = int(input("Nhập số m: "))
n = int(input("Nhập số n: "))
def UCBC(m,n):
    print("UCLN của", m, "và", n, "là:", UCLN(m, n))
    print("BCNN của", m, "và", n, "là:", BCNN(m, n))
UCBC(m,n)