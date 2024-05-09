import random

a1, a2, b1, b2, topA, topB = 0, 0, 0, 0, 0, 0

a1 = random.randrange(1, 7)
a2 = random.randrange(1, 7)
b1 = random.randrange(1, 7)
b2 = random.randrange(1, 7)
print("A의 주사위 숫자는 %d %d입니다." % (a1, a2))
print("B의 주사위 숫자는 %d %d입니다." % (b1, b2))

if a1 >= a2:
    topA = a1
else:
    topA = a2

if b1 >= b2:
    topB = b1
else:
    topB = b2


if topA > topB:
    print("A가 이겼네요.")
elif topA == topB:
    print("둘이 비겼네요.")
else:
    print("B가 이겼네요.")