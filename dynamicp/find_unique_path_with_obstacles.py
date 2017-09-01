# Unique paths in a Grid with Obstacles
# Given a grid of size m * n, let us assume you are starting at (1, 1) and your goal is to reach (m, n). At any instance, if you are on (x, y), you can either go to (x, y + 1) or (x + 1, y).
# Now consider if some obstacles are added to the grids. How many unique paths would there be?
# An obstacle and empty space are marked as 1 and 0 respectively in the grid.
#
# Examples:
#
# Input: [[0, 0, 0],
#         [0, 1, 0],
#         [0, 0, 0]]
# Output : 2
# There is only one obstacle in the middle.
# http://www.geeksforgeeks.org/unique-paths-in-a-grid-with-obstacles/

def unique_path_w_obstacles(a):
    # create 2d matrix of zeros
    paths = [[0 for x in a[0]] for i in a]

    # init left corner if no obstacle there
    if a[0][0] == 0:
        paths[0][0] = 1

    # init first column of 2d matrix
    for i in range(1, len(a)):
        if a[i][0] == 0: # not obstacle
            paths[i][0] = paths[i-1][0]

    # init first row of matrix
    for i in range(1, len(a[0])):
        if a[0][i] == 0: # not obstacle
            paths[0][i] = paths[0][i-1]

    for i in range(1, len(a)):
        for j in range(1, len(a[0])):
            # if current cell is not obstacle
            if a[i][j] == 0:
                paths[i][j] = paths[i-1][j] + paths[i][j-1]

    # return corner value of matrix
    return paths

mat = [[0, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0]]
print unique_path_w_obstacles(mat)
