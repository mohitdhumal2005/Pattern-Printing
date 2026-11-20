
rows = 5

for i in range(1, rows + 1):
    spaces = " " * ((rows - i) * 2)       # leading padding that pushes stars right
    stars = " ".join(["*"] * i)           # the stars of this row
    print(spaces + stars)
