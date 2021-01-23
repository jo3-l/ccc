n = int(input())

lines = []
for _ in range(n):
    n, c = input().split(" ")
    n = int(n)
    # This looks a bit funky, but Python has overloaded the * operator on
    # strings to repeat the string.
    lines.append(c * n)

print("\n".join(lines))
