import numpy as np

# Read input
with open("Advent of Code Day 8 - Input.txt", "r") as my_file:
    data = my_file.read().split()

# print(data)

# Transform the data into a grid of lists containing integers.
# list() transforms the lines into lists.
# map () transforms the lists into int.
# Since map() doesn't turn the result into a list, we need to use another list().

grid = []

for line in data:
    grid.append(list(map(int, list(line))))

# print(grid)

n_of_rows = len(grid)
n_of_columns = len(grid[0])

# Transform the grid into an array
grid = np.array(grid)

# print(grid)

answer = 0

# Iterate over each tree
# The outer trees should be automatically added to the answer, i.e.
#       if i or j = 0
#       i = n_of_rows
#       j = n_of_columns

for i in range(n_of_rows):
    for j in range(n_of_columns):
        a = grid[i, j]

        # We check for each tree we iterate over whether it's visible from any direction
        # Check whether a tree is visible from the left, i.e. there are no trees from the left that are equally as tall or taller
        # We check all the trees up to but no including j
        if j == 0 or np.amax(grid[i, :j]) < a:
            answer += 1

        # Check in a similar way from the right
        elif j == n_of_columns - 1 or np.amax(grid[i, (j+1):]) < a:
            answer += 1

        # Check in a similar way from the top
        elif i == 0 or np.amax(grid[:i, j]) < a:
            answer += 1

        # Check in a similar way from the bottom
        elif i == n_of_rows - 1 or np.amax(grid[(i+1):, j]) < a:
            answer += 1

print("Answer Day 8, Part 1 is", answer)

#-----------------------------------------------------------------------#
scenic_score = 0
highest_scenic_score = []

trees_from_left = []
trees_from_right = []
trees_from_top = []
trees_from_bottom = []

# Iterate over the trees
for i in range(n_of_rows):
    for j in range(n_of_columns):
        a = grid[i, j]

        # List all the trees from each side of the tree a
        trees_from_left = [grid[i, j-m] for m in range(1, j+1)]
        trees_from_right = [grid[i, j+m] for m in range(1, n_of_columns-j)]
        trees_from_top = [grid[i-m, j] for m in range(1, i+1)]
        trees_from_bottom = [grid[i+m, j] for m in range(1, n_of_rows-i)]

        # Calculate the scenic score
        scenic_score = 1
        for lst in (trees_from_left, trees_from_right, trees_from_top, trees_from_bottom):
            tracker = 0
            for n in range(len(lst)):
                if lst[n] < a:
                    tracker += 1
                elif lst[n] >= a:
                    tracker += 1
                    break

            scenic_score *= tracker

        highest_scenic_score.append(scenic_score)

print("Answer Day 8, Part 2 is", max(highest_scenic_score))
