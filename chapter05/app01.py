import random

s_count = 0
l_count = 0

while True:
    s_count += 1
    numbers = []
    for num in range(1, 7):
        numbers.append(random.randrange(1, 7))

    if 1 in numbers:
        if 2 in numbers:
            if 3 in numbers:
                if 4 in numbers:
                    if 5 in numbers:
                        if 6 in numbers:
                            l_count += 1

    if numbers[0] == numbers[1] == numbers[2] == numbers[3] == numbers[4] == numbers[5]:
        break

print("숫자: %d %d %d %d %d %d" % (numbers[0], numbers[1], numbers[2], numbers[3], numbers[4], numbers[5]))
print("같은 숫자가 나올 때까지 주사위를 던진 횟수: %d회" % s_count)
print("연속 번호가 나온 횟수: %d회" % l_count)