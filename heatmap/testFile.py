
grid = np.empty([int(gridSize), int(gridSize)])
grid.fill(0)

row = 0

for i in range(0, cells):

    column = i% gridSize
    grid[row][column] = cnt

    if (column == 4):
        row += row
