num1 = int(input("첫 번째 숫자를 입력하세요: "))
num2 = int(input("두 번째 숫자를 입력하세요: "))
plus = int(input("더할 숫자를 입력하세요: "))
ans = 0

for i in range(num1, num2+1, plus):
    ans += i

print("%d + %d + ... + %d는 %d입니다." % (num1, num1 + plus, num2, ans))