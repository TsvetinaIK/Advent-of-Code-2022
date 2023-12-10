from collections import defaultdict

# Read input
with open("Advent of Code Day 7 - Input.txt") as my_file:
    commands = my_file.read().strip().split("\n$ ")

# Remove the "$" from the beginning of the first line
commands[0] = commands[0].strip("$ ")

# Variables that will store the current path as both list and string
current_path = []
current_path_string = ""

# Dictionaries that will store the sizes and contained directories found in each path
my_dict_sizes = defaultdict(int)
my_dict_dir = defaultdict(list)

# Parse the input according to the commands


def parse(commandlines):
    # Split the commands
    lines = commandlines.split("\n")
    command = lines[0]
    output = lines[1:]

    parts = command.split(" ")
    op = parts[0]
    if op == "cd":
        # If the command is "cd..", we go back to the previous directory so we remove one item from the list
        if parts[1] == "..":
            current_path.pop()
        # Otherwise the command is "cd x" so we need to add another directory
        else:
            current_path.append(parts[1])

        return

    # In order to use the current path as a key in a dictionary, we need to transform it from a list to a string
    current_path_string = "/".join(current_path)
    assert op == "ls"

    sizes = []
    for line in output:
        if not line.startswith("dir"):
            sizes.append(int(line.split(" ")[0]))
        else:
            dir_name = line.split(" ")[1]
            my_dict_dir[current_path_string].append(
                f"{current_path_string}/{dir_name}")

    my_dict_sizes[current_path_string] = sum(sizes)


# We run the function for the entire input
for command in commands:
    parse(command)

# Create a recursive function in order to look for all paths and their subpaths that will correspond to a certain condition


def search(current_path_string):
    size = my_dict_sizes[current_path_string]
    for child in my_dict_dir[current_path_string]:
        size += search(child)
    return size


answer = 0
for path in my_dict_sizes:
    if search(path) <= 100000:
        answer += search(path)

print("Answer Day 7, Path 1 is", answer)

#------------------------------------------------------------------#

# Find the total space that is used at the moment
total_space_used = 0

for command in commands:
    # If the command is "ls ..", we add to the lists
    if command[:2] == "ls":
        command = command.split("\n")
        # Split the resulting list further by " "
        for i in command:
            i = i.split(" ")
            if i[0].isdigit():
                total_space_used += int(i[0])

# print(total_space_used)

total_space_needed = 70000000-30000000
min_amount_to_delete = total_space_used - total_space_needed

answer2 = 1 << 60
for path in my_dict_sizes:
    size = search(path)
    if size >= min_amount_to_delete:
        answer2 = min(answer2, size)

print("Answer Day 7, Part 2 is", answer2)
