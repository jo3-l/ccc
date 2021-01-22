# This implementation gets 13/15, still looking for ways to get 15/15
import collections

max_rows = int(input())
max_cols = int(input())

# Value symbolizing the end of the room.
END_ROOM_TOKEN = -1

matrix = []
for _ in range(max_rows):
    matrix.append([int(x) for x in input().split(" ")])

matrix[max_rows - 1][max_cols - 1] = END_ROOM_TOKEN


# Returns an iterator over the cell values that can be jumped to from the given
# cell value.
def possible_moves(val):
    if (max_rows * max_cols) < val:
        return

    # TODO: find the proper range for this using math
    # 1000^2 > 1000000... hacky, but it works so :/
    for possible_row in range(1, 1001):
        if possible_row > max_rows:
            break

        if val % possible_row == 0:
            matching_col = val // possible_row
            if matching_col > max_cols:
                continue

            # Subtract one because our rows and columns are 1-based.
            yield matrix[possible_row - 1][matching_col - 1]
            if possible_row != matching_col:
                if matching_col > max_rows or possible_row > max_cols:
                    continue
                yield matrix[matching_col - 1][possible_row - 1]


def bfs(row, col):
    visited = set()
    queue = collections.deque([matrix[row][col]])
    while queue:
        val = queue.popleft()
        for possible_val in possible_moves(val):
            if possible_val == END_ROOM_TOKEN:
                return True
            if possible_val not in visited:
                visited.add(possible_val)
                queue.append(possible_val)

    return False


print("yes" if bfs(0, 0) else "no")
