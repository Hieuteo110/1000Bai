n=int(input("Nhập vào tháng: "))
if n<1 or n>12:
    print("Nhập tháng không hợp lệ")
else:
    quy=(n-1)//3+1
    print(f"Tháng {n} thuộc Quý {quy}")