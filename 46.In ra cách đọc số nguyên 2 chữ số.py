import sys
def cach_doc(n):
    if n==00:
        return "Không"
    b=n%10
    a=n//10
    if b==1:
        b="Mốt"
    elif b==2:
        b="Hai"
    elif b==3:
        b="Ba"
    elif b==4:
        b="Tư"
    elif b==5:
        b="Lăm"
    elif b==6:
        b="Sáu"
    elif b==7:
        b="Bảy"
    elif b==8:
        b="Tám"
    elif b==9:
        b="Chín"
    if a==2:
        a="Hai mươi"
    elif a==3:
        a="Ba mươi"
    elif a==4:
        a="Bốn mươi"
        if b=="Tư":
            b="Bốn"
    elif a==5:
        a="Năm mươi"
    elif a==6:
        a="Sáu mươi"
    elif a==7:
        a="Bảy mươi"
    elif a==8:
        a="Tám mươi"
    elif a==9:
        a="Chín mươi"
    if a==1:
        a="Mười"
        if b=="Tư":
            b="Bốn"
        elif b=="Mốt":
            b="Một"
    t=(f"{a} {b}")
    return t
running=True
dem=0
while running:
    n=int(input("Nhập vào 1 số nguyên có 2 chữ số: "))
    if len(str(n))>2:
        dem+=1
        if dem==3:
            print("""
=======================
Đã nhập sai 3 lần
Chương trình đã bị dừng
=======================
""")
            sys.exit()
        print("""
=================================================
Đã nhập số nguyên vượt quá 2 chữ số, thao tác lại
=================================================
""")
    else:
        running=False
print(f"Cách đọc của số {n}: {cach_doc(n)}")