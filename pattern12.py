# *                 *
# * *             * *
# * * *         * * *
# * * * *     * * * *
# * * * * * * * * * *
# * * * *     * * * *
# * * *         * * *
# * *             * *
# *                 *
n = 5
width = 2 * n


def print_row(i):
    """Draw one row of the butterfly that has i stars on each wing."""
    line = []
    for col in range(width):
        # a cell is a star if it's in the first i columns or the last i columns
        if col < i or col >= width - i:
            line.append("*")
        else:
            line.append(" ")          # the gap between the wings
    print(" ".join(line))


# Top half - wings getting wider
for i in range(1, n + 1):
    print_row(i)

# Bottom half - wings getting narrower (skip n so the middle row isn't repeated)
for i in range(n - 1, 0, -1):
    print_row(i)
