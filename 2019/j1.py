a3, a2, a1 = int(input()), int(input()), int(input())
b3, b2, b1 = int(input()), int(input()), int(input())

a_total = a3 * 3 + a2 * 2 + a1
b_total = b3 * 3 + b2 * 2 + b1

if a_total > b_total:
    print("A")
elif a_total == b_total:
    print("T")
else:
    print("B")

