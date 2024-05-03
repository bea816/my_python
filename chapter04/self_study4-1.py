money, b50000, b10000, b5000, b1000 = 0, 0, 0, 0, 0

money = int(input("지폐로 교환할 돈은 얼마? "))

b50000 = money // 50000
money %= 50000
b10000 = money // 10000
money %= 10000
b5000 = money // 5000
money %= 5000
b1000 = money // 1000
money %= 1000

print("\n 50000원짜리 ==> %d장" % b50000)
print(" 10000원짜리 ==> %d장" % b10000)
print(" 5000원짜리 ==> %d장" % b5000)
print(" 1000원짜리 ==> %d장" % b1000)
print(" 지폐로 바꾸지 못한 잔돈 ==> %d원 \n" % money)