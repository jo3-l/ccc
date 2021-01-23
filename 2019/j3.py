repeated_count = int(input())

encoded_lines = []
for _ in range(repeated_count):
    line = input()
    pairs = []

    # Position in line
    i = 0
    # We use a `while` loop as we may increment `i` within the loop body.
    while i < len(line):
        repeated_count = 0
        c = line[i]
        # Increment the position and the number of repeated characters while
        # we're not out of range and the character is the same...
        while i < len(line) and line[i] == c:
            repeated_count += 1
            i += 1

        # And then append the number of times the character was repeated,
        # followed by the character.
        pairs.append(f"{repeated_count} {c}")

    # Then add the encoded line.
    encoded_lines.append(" ".join(pairs))

# Finally, print all encoded lines.
print("\n".join(encoded_lines))
