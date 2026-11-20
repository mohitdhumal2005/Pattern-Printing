# * * * *
# * * * *
# * * * *
# * * * *
    
size = 4

for row in range(size):          # outer loop -> walks down the rows
    line = []                    # I collect the stars of this row here
    for col in range(size):      # inner loop -> walks across the columns
        line.append("*")
    print(" ".join(line))        # join with a space so it looks like "* * * *"
                                 # (join also avoids a messy trailing space)
