# NOTICE: This implementation is incomplete and only gets 13/15 points on DMOJ.
# I'm still working on further optimizations to get this to 15/15.
import collections
import math

# Value symbolizing the end of the room.
END_ROOM_TOKEN = -1

# Remember that these are 1-based.
max_rows = int(input())
max_cols = int(input())

matrix = []
for _ in range(max_rows):
    matrix.append([int(x) for x in input().split(" ")])

# Change the end room value to our special token so we can differentiate it from
# other cells given just the value.
matrix[max_rows - 1][max_cols - 1] = END_ROOM_TOKEN


# Returns an iterator of valid cell values to move to from the given value.
def valid_moves(val):
    min_bound = math.ceil(val / max(max_cols, max_rows))
    # +1 because `range` is exclusive on its upper bound.
    max_bound = max_rows + 1

    # This is probably where we can optimize more, but I haven't been able to
    # pinpoint what exactly yet.
    for possible_row in range(min_bound, max_bound):
        if val % possible_row == 0:
            matching_col = val // possible_row
            # If the column is out of range...
            if matching_col > max_cols:
                continue

            # Remember to subtract one because our rows and columns are 1-based
            # in the loop.
            yield matrix[possible_row - 1][matching_col - 1]
            # We should also see if the coordinate pair works when it is
            # reversed - given (1, 3), (3, 1) may also be valid.
            if possible_row != matching_col:
                if matching_col > max_rows or possible_row > max_cols:
                    continue
                yield matrix[matching_col - 1][possible_row - 1]


# bfs() uses a breadth-first search to determine whether we can escape out of
# the room. DMOJ shows a RecursionError if we use the less complex depth-first
# search approach.
def bfs(initial_val):
    # A set of cell values we've already visited, so we don't accidentally go
    # into an infinite loop / do more work than we need to.
    visited = set()

    # A deque guarantees constant time complexity for appends and pops on either
    # end, which fits our use-case very well.
    queue = collections.deque([initial_val])

    # While the queue is not empty...
    while queue:
        # Retrieve the cell value that was added first...
        current_val = queue.popleft()
        # And iterate over its possible moves...
        for move in valid_moves(current_val):
            # If we can get to the end cell, return early...
            if move == END_ROOM_TOKEN:
                return True
            # Otherwise, if we haven't made this move before...
            if move not in visited:
                # Then mark it as visited and append it to the queue to traverse
                # later.
                visited.add(move)
                queue.append(move)

    # If we've gotten to this point, it implies that there is no way to escape
    # out of the maze.
    return False


print("yes" if bfs(matrix[0][0]) else "no")
