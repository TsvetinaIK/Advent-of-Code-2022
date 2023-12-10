# Read input
with open("Advent of Code Day 1 - Input.txt", "r") as my_file:
    lines = my_file.read().strip().split("\n")

# print(lines)

l_of_lines = []
l_of_calculated_kcal = []
n_of_kcal = 0

# Convert the data to integers
for line in lines:
    if line == "":
        l_of_lines.append(0)
    else:
        l_of_lines.append(int(line))

# Iterate through the data and add the number of calories for each elf
# Then add the total for each elf as an entry in the list called "l_of_calculated_kcal"
for line in l_of_lines:
    if line != 0:
        n_of_kcal += int(line)
    else:
        l_of_calculated_kcal.append(n_of_kcal)
        n_of_kcal = 0

# Find the max in the resulting list and, optionally, find the index, i.e. the number of the elf
max_n_of_kcal = max(l_of_calculated_kcal)
index_elf = l_of_calculated_kcal.index(max_n_of_kcal)

print("Answer Day 1, Part 1 is", max_n_of_kcal,
      "kcal carried by elf #" + str(index_elf) + ".")

#-------------------------------------------------------------------------------#

# Sort the list
l_of_calculated_kcal.sort()

# Calculate the kcal for the top three elves
print("Answer Day 1, Part 2 is", l_of_calculated_kcal[-1]+l_of_calculated_kcal[-2] +
      l_of_calculated_kcal[-3], "kcal carried by the top three elves.")
