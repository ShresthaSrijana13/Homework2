# Srijana Shrestha
# 1918305
a = int(input())
b = int(input())
c = int(input())

d = int(input())
e = int(input())
f = int(input())


def val1(x, y):
    return a * x + b * y - c


def val2(x, y):
    return d * x + e * y - f


sol_x = 1
sol_y = 1

for x in range(-10, 11, 1):
    for y in range(-10, 11, 1):
        if val1(x, y) == val2(x, y) and val1(x, y) == 0:
            sol_x = x
            sol_y = y

if sol_x != 1:
    print(sol_x, sol_y)

else:
    print('No solution')
