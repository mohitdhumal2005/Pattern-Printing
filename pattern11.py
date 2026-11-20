# *
# * *
# *   *
# *     *
# * * * * *

rows = 5

for i in range(1, rows + 1):
    line = []
    for col in range(1, i + 1):
        if col == 1 or col == i or i == rows:
            line.append("*")
        else:
            line.append(" ")          # hollow interior
    print(" ".join(line))
