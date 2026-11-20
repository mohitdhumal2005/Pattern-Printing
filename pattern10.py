# * * * * *
# *       *
# *       *
# *       *
# * * * * *

size = 5

for row in range(size):
    line = []
    for col in range(size):
        on_border = (row == 0 or row == size - 1 or col == 0 or col == size - 1)
        if on_border:
            line.append("*")
        else:
            line.append(" ")          # keeps the hollow part the right width
    print(" ".join(line))
