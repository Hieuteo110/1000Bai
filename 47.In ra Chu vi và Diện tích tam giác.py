import math
running = True
while running:
    a = float(input("Nhập cạnh a: "))
    b = float(input("Nhập cạnh b: "))
    c = float(input("Nhập cạnh c: "))
    if a <= 0 or b <= 0 or c <= 0:
        print("""
=================================================
Các cạnh tam giác không hợp lệ, vui lòng nhập lại
=================================================

""")
    else:
        running=False
P = a + b + c
p = (a + b + c) / 2
S = math.sqrt(p * (p - a) * (p - b) * (p - c))
print("Chu vi tam giác =", P)
print(f"Diện tích tam giác = {S}")  