#         *
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *
#   * * * * * * *
#     * * * * *
#       * * *
#         *

rows = 5   # number of rows in the top half (includes the widest row)

# ---- Top half: growing pyramid ----
for i in range(1, rows + 1):
    spaces = " " * ((rows - i) * 2)
    stars = " ".join(["*"] * (2 * i - 1))
    print(spaces + stars)

# ---- Bottom half: shrinking pyramid ----
# I start from rows - 1 (not rows) so the widest line isn't printed twice.
for i in range(rows - 1, 0, -1):
    spaces = " " * ((rows - i) * 2)
    stars = " ".join(["*"] * (2 * i - 1))
    print(spaces + stars)
