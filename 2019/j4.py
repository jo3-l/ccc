v = input()

num_horizontal = 0
num_vertical = 0
for c in v:
    if c == "H":
        num_horizontal += 1
    else:
        num_vertical += 1

# Strings for easier formatting later.
square = [["1", "2"], ["3", "4"]]

# Two vertical flips -> no change. Two horizontal flips -> no change. Therefore,
# we only need to handle the case where the numbers are odd.
if num_horizontal % 2 == 1:
    square.reverse()

if num_vertical % 2 == 1:
    square[0].reverse()
    square[1].reverse()

print(f"{' '.join(square[0])}\n{' '.join(square[1])}")

