
# 2d lists are essentially lists of lists
# for example
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

# the example now has 4 rows with three columns
# to access a specific element in the list by reference to the row and column
print(number_grid[1][2])  # This will print row 1, column 2

# to print row
print(number_grid[2])

# this for loop will read out each row of the grid
for row in number_grid:
    print(row)


# Nested for loop will read each element of the grid
# each column of row 0 will be read before moving onto the next row
for row in number_grid:
    for col in row:
        print(col)


