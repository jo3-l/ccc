# This solution grabs 11/15 available points, others fail with RecursionError...

# A set of already visited cell values. Given that we have already visited the
# cell with the value X, it is unnecessary to revisit it as all valid moves
# should already have been played.
already_visited = set()

max_rows = int(input())
max_cols = int(input())

matrix = []
for _ in range(max_rows):
    matrix.append([int(x) for x in input().split(" ")])


# Returns an iterator over the possible row and column pairs (0-based, not
# 1-based) that are valid moves from a cell with the given value.
def possible_moves(row, col):
    val = matrix[row][col]
    if val in already_visited:
        # Already visited a cell with this value.
        return

    if (max_rows * max_cols) < val:
        return

    already_visited.add(val)

    # 1001^2 > 1000000... hacky, but it works so :/
    for possible_row in range(1, 1001):
        if possible_row > max_rows:
            break

        if val % possible_row == 0:
            matching_col = val // possible_row
            if matching_col > max_cols:
                continue

            # Subtract one because our rows and columns are 1-based.
            yield possible_row - 1, matching_col - 1
            if possible_row != matching_col:
                if matching_col > max_rows or possible_row > max_cols:
                    continue
                yield matching_col - 1, possible_row - 1


def traverse(row, col):
    # If it's the exit...
    if (row == max_rows - 1) and (col == max_cols - 1):
        return True

    for new_row, new_col in possible_moves(row, col):
        if traverse(new_row, new_col):
            return True

    return False


print("yes" if traverse(0, 0) else "no")
