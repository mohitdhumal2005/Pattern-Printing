
rows = 5

for i in range(1, rows + 1):
    line = []
    for _ in range(i):               # repeat i times
        line.append(str(i))          # always the same number: the row number
    print(" ".join(line))
