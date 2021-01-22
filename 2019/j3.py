repeated_count = int(input())

encoded_lines = []
for _ in range(repeated_count):
    line = input()
    pairs = []

    # Position in line
    i = 0
    while i < len(line):
        # Number of repeated characters
        repeated_count = 0
        # Character to look for
        c = line[i]
        # Increment the position and the number of repeated characters while
        # we're not out of range and the character is the same...
        while i < len(line) and line[i] == c:
            repeated_count += 1
            i += 1
        # And then append the number of times the character was repeated,
        # followed by the character.
        pairs.append(f"{repeated_count} {c}")

    # And then add the encoded line.
    encoded_lines.append(" ".join(pairs))

# And then print all the encoded lines.
print("\n".join(encoded_lines))
