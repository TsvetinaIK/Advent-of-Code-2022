# Read input
with open("Advent of Code Day 10 - Input.txt", "r") as my_file:
    data = my_file.read().strip().split("\n")

# print(data)

# We set the n_of_cycles to 0 due to zero-based numbering. Thus, if we need the data for cycle 20, we need to look for index 19
command = 0
value_of_x = 1
addition_to_x = 0

# Create a list with the value of X. We need to create the whole list in advance so that we can insert in certain positions
# Therefore we use len(data) and two extra positions for commands executed
# The first entry is equal to the value of X
l_of_values_of_X = [0]*(len(data)+2)
l_of_values_of_X[0] = 1

# Create a list with all the commands from addx
l_of_additions = [0]*(len(data)+2)

# Create a list mapping the list of cycles to number of commands
n_of_cycles = 1
l_of_cycles = []


for line in data:
    # "noop" takes one cycle to complete and makes no other changes
    if line == "noop":
        l_of_cycles.append(n_of_cycles)
        n_of_cycles += 1

    # "addx" takes two cycles to complete and adds a value to X
    if line[:4] == "addx":
        addition_to_x = int(line[5:])
        l_of_additions[command+2] = addition_to_x
        l_of_cycles.append(n_of_cycles)
        n_of_cycles += 2
    command += 1

for i in range(1, len(l_of_additions)):
    l_of_values_of_X[i] = l_of_values_of_X[i-1] + l_of_additions[i]

# Find the number of cycles corresponding to which command and value of X:
l_of_cycles_needed = [20, 100, 180, 220]
# l_of_cycles_needed = [20, 60, 100, 140, 180, 220]
l_of_indices_needed = []

index_for_20th = l_of_cycles.index(20)
index_for_60th = l_of_cycles.index(59)
index_for_100th = l_of_cycles.index(100)
index_for_140th = l_of_cycles.index(139)
index_for_180th = l_of_cycles.index(180)
index_for_220th = l_of_cycles.index(220)

strength20 = 20 * l_of_values_of_X[index_for_20th+1]
strength60 = 60 * l_of_values_of_X[index_for_60th+1]
strength100 = 100 * l_of_values_of_X[index_for_100th+1]
strength140 = 140 * l_of_values_of_X[index_for_140th+1]
strength180 = 180 * l_of_values_of_X[index_for_180th+1]
strength220 = 220 * l_of_values_of_X[index_for_220th+1]

answer = strength20 + strength60 + strength100 + \
    strength140 + strength180 + strength220

print("Answer Day 10, Part 1 is", answer)
