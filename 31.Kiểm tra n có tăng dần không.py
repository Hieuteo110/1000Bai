n = int(input("Nhập số n: "))
last_digit = 10
check = True
while n > 0:
    i = n % 10
    if i>last_digit:
        check=False
        break
    last_digit=i
    n //= 10
if check:
    print("Đúng")
else:
    print("Sai")