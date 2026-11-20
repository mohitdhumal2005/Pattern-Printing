# * * * * *
# * * * *
# * * *
# * *
# *
rows = 5

for i in range(rows, 0, -1):     # 5, 4, 3, 2, 1 (step of -1 counts backwards)
    line = []
    for _ in range(i):           # stars in this row = current value of i
        line.append("*")
    print(" ".join(line))
