def nhuan(n):
    check=False
    if n%400==0 or (n%4==0 and n%100!=0):
        check=True
    return check
def thang31(n):
    check=False
    if n==1 or n== 3 or n==5 or n==7 or n==8 or n==10 or n==12:
        check=True
    return check
def thang30(n):
    check=False
    if n==4 or n==6 or n==9 or n==11:
        check=True
    return check
running=True
while running:
    day=int(input("Nhập vào ngày : "))
    month=int(input("Nhập vào tháng : "))
    year=int(input("Nhập vào năm : "))
    if day>=32 or month >=13 or day<1 or month<1 or year<1:
        print("""
==========================
Vui lòng nhập lại thông số
==========================

""")
    else:
        running=False
day+=1
if nhuan(year) and ((day==30)and month==2):
    day=1
    month+=1
if day==32 and month==12:
    month=1
    day=1
    year+=1
elif ((day==31) and thang30(month)) or ((day==32)and thang31(month)):
    day=1 
    month+=1
print(f"Ngày tiếp theo là ngày {day} tháng {month} năm {year}")