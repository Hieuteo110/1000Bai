a=float(input("Nhập cạnh a = "))
b=float(input("Nhập cạnh b = "))
c=float(input("Nhập cạnh c = "))
def kt(a,b,c):
    if a*a==b*b+c*c or b*b==a*a+c*c or c*c==a*a+b*b:
        print("Đây là tam giác vuông")
    elif a==b==c:
        print("Đây là tam giác đều")
    elif a==b or a==c or b==c:
        print("Đây là tam giác cân")
    elif a*a>b*b+c*c or b*b>a*a+c*c or c*c>a*a+b*b:
        print("Đây là tam giác tù")
    elif a*a<b*b+c*c or b*b<a*a+c*c or c*c<a*a+b*b:
        print("Đây là tam giác nhọn")
if a<b+c and b<a+c and c<a+b:
    kt(a,b,c)
else:
    print("Các cạnh không hợp lệ")
