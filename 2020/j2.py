p, n, r = int(input()), int(input()), int(input())

total = n
day = 0
while total <= p:
    day += 1
    # The number of infected people is a geometric series where the coefficient
    # is N and the ratio is R.
    total += (r ** day) * n

print(day)
