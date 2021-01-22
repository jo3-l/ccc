max_rows, max_cols = int(input()), int(input())

# Set of cell coordinates we have already visited
already_visited = set()
# Cache of cell -> cells we can jump to from said cell
jump_cache = {}


def can_jump(val):
    if val in jump_cache:
        return jump_cache[val]

    # Starting from 1 because that's just easier to reason about
    for row in range(1, max_rows + 1):
        for col in range(1, (val // row) + 1):
            pass

