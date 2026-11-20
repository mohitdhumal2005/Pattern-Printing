# * * * * * * * * *
#   * * * * * * *
#     * * * * *
#       * * *
#         *

rows = 5

for i in range(rows, 0, -1):               # count backwards 5..1
    spaces = " " * ((rows - i) * 2)        # starts at 0 and grows each row
    stars = " ".join(["*"] * (2 * i - 1))  # 9, 7, 5, 3, 1
    print(spaces + stars)
