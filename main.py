import math

print("a = ")
a = int(input())
print("b = ")
b = int(input())
print("c = ")
c = int(input())

d = b*b - 4*a*c
if d > 0:
    x1 = (-b + math.sqrt(b*b - 4*a*c))/2/a
    x2 = (-b - math.sqrt(b*b - 4*a*c))/2/a
    print("x1 = ", x1)
    print("x2 = ", x2)
elif d == 0:
    x1 = -b/2/a
    print("x = ", x1)
else:
    print("Да тут косяк, подумай хорошенько")
