num = int(input("숫자를 입력하세요: "))
box = 0

for i in range(2, num):
    if num % i == 0:
        box = 1

if box == 0:
    print("%d는 소수입니다." % num)
else:
    print("%d는 소수가 아닙니다." % num)