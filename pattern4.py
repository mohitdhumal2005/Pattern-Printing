
rows = 5

for i in range(1, rows + 1):         # i = which row we're on
    line = []
    for num in range(1, i + 1):      # counts 1..i in this row
        line.append(str(num))        # numbers must become text before joining
    print(" ".join(line))
