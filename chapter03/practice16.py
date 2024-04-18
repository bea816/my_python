#아스키코드를 활용해 문자와 숫자 구분
val = input("글자 입력: ")

if val >= '0' and val <= '1':
    print("2진수 또는 8진수 또는 10진수 또는 16진수 입니다.")
elif val > '1' and val <= '7':
    print("8진수 또는 10진수 또는 16진수 입니다.")
elif val > '7' and val <= '9':
    print("10진수 또는 16진수 입니다.")
elif val >= 'A' and val <= 'F':
    print("16진수 입니다.")
else:
    print("숫자가 아닙니다.")