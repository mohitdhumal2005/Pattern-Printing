#         *
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *

rows = 5

for i in range(1, rows + 1):
    spaces = " " * ((rows - i) * 2)       # 8, 6, 4, 2, 0 spaces
    stars = " ".join(["*"] * (2 * i - 1))  # 1, 3, 5, 7, 9 stars
    print(spaces + stars)
