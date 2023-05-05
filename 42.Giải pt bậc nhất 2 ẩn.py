a1 = float(input("Nhập a1: "))
b1 = float(input("Nhập b1: "))
c1 = float(input("Nhập c1: "))
a2 = float(input("Nhập a2: "))
b2 = float(input("Nhập b2: "))
c2 = float(input("Nhập c2: "))
if a1 == 0:
    a1, a2 = a2, a1
    b1, b2 = b2, b1
    c1, c2 = c2, c1
m = a2 / a1
b2 -= m * b1
c2 -= m * c1
x2 = c2 / b2
x1 = (c1 - b1 * x2) / a1
print(f"""Hệ phương trình có nghiệm:
(x;y) = ({round(x1,1)};{round(x2,1)})""")