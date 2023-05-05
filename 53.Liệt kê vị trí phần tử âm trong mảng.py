n = int(input("Nhap so phan tu cua mang: "))
a = []
for i in range(n):
    print(f"Nhap gia tri phan tu thu {i}: ", end="")
    a.append(int(input()))
found_negative = False
for i in range(n):
    if a[i] < 0:
        print(f"Vi tri gia tri am {a[i]} trong mang la: {i}")
        found_negative = True
if not found_negative:
    print("Khong co gia tri am trong mang")