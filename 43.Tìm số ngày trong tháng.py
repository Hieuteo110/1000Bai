import calendar
year = int(input("Nhập năm: "))
month = int(input("Nhập tháng: "))
days = calendar.monthrange(year, month)[1]
print(f"Số ngày trong tháng {month} năm {year} là: {days}")