import sys
def nhuan(n):
    check=False
    if n%400==0 or (n%4==0 and n%100!=0):
        check=True
    return check
running=True
dem=0
while running:
    y1=int(input("Nhập y1: "))
    y2=int(input("Nhập y2: "))
    if y2<=y1:
        dem+=1
        if dem==3:
            print("""
========================================
Bạn đã nhập sai thông số 3 lần liên tiếp
Chương trình đã bị dừng
========================================

""")
            sys.exit()
        print("""
==========================
Vui lòng nhập lại thông số
==========================

""")
    else:
        running=False
        dem=0
for i in range(y1,y2+1):
    if nhuan(i):
        dem+=1
print(f"Số năm nhuận trong khoảng {y1} đến {y2}: {dem} năm")