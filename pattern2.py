# *
# * *
# * * *
# * * * *
# * * * * *

rows = 5

for i in range(1, rows + 1):     # start at 1 so row number == star count
    line = []
    for _ in range(i):           # print as many stars as the row number
        line.append("*")
    print(" ".join(line))
