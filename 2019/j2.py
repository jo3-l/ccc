n = int(input())

lines = []
for _ in range(n):
    n, c = input().split(" ")
    n = int(n)
    lines.append(c * n)

print("\n".join(lines))
