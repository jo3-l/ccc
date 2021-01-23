t, s = input(), input()


def cyclic_shifts(s):
    cur = s
    # The logic here is to shift the string's characters one place to the left
    # until it goes back to its original state, at which point we will have
    # obtained all cyclic shifts of this string.
    for _ in range(len(s)):
        cur = cur[1:] + cur[0]
        yield cur


contains = False
for cyclic_shift in cyclic_shifts(s):
    if cyclic_shift in t:
        contains = True
        break

print("yes" if contains else "no")
