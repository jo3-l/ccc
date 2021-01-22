p, n, r = int(input()), int(input()), int(input())

total = n
prev_total = 0
day = 0
while total <= p:
    (prev_total, total) = (total, total + (total - prev_total) * r)
    day += 1

print(day)
