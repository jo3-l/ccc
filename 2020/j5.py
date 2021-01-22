# This implementation gets 13/15, still looking for ways to get 15/15
import collections

visited = set()

max_rows = int(input())
max_cols = int(input())

matrix = []
for _ in range(max_rows):
    matrix.append([int(x) for x in input().split(" ")])


# Returns an iterator over the possible row and column pairs (0-based, not
# 1-based) that are valid moves from a cell with the given value.
def possible_moves(row, col):
    val = matrix[row][col]

    if (max_rows * max_cols) < val:
        return

    # TODO: find the proper range for this using math
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


def bfs(row, col):
    queue = collections.deque([(row, col)])
    while queue:
        vertex = queue.popleft()
        for row, col in possible_moves(*vertex):
            val = matrix[row][col]
            if row == max_rows - 1 and col == max_cols - 1:
                return True
            if val not in visited:
                visited.add(val)
                queue.append((row, col))

    return False


print("yes" if bfs(0, 0) else "no")
