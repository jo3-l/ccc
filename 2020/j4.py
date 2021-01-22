def iter_cyclic_shifts(s):
    cur = s
    for _ in range(len(s)):
        cur = cur[1:] + cur[0]
        yield cur


t, s = input(), input()

contains = False
for cyclic_shift in iter_cyclic_shifts(s):
    if cyclic_shift in t:
        contains = True
        break

print("yes" if contains else "no")
