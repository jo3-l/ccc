import math

n = int(input())

max_x = -1
max_y = -1

min_x = 101
min_y = 101

for _ in range(n):
    x, y = [int(x) for x in input().split(",")]
    if x > max_x:
        max_x = x
    elif x < min_x:
        min_x = x

    if y > max_y:
        max_y = y
    elif y < min_y:
        min_y = y

print(f"{min_x - 1},{min_y - 1}")
print(f"{max_x + 1},{max_y + 1}")
