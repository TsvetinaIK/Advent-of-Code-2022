"""
The difference between the solutions for Part 1 and Part 2 is that for

# Remove items from stack_reduced

In Part 1 we have

    for j in range(0, q_moved):
        if stack_reduced == 1:
            item_moved.insert(0, stack_1[0])
            stack_1.pop(0)

In Part 2 we have
    for j in range(0, q_moved):
        if stack_reduced == 1:
            item_moved.append(stack_1[0])
            stack_1.pop(0)

"""

# Read input
# .strip() is not used in order to keep the white space which defines the stacks
with open('Advent of Code Day 5 - Input.txt', "r") as my_file:
    data = my_file.read().split("\n")

# print(data)

n_of_stacks = 0
stacks = []
stack_1 = []
stack_2 = []
stack_3 = []
stack_4 = []
stack_5 = []
stack_6 = []
stack_7 = []
stack_8 = []
stack_9 = []
empty_space = ['', '', '', '']

# Create a list of the stacks containing all the data for the stacks
for line in data:
    if line[:2] == " 1":
        break
    else:
        line = line.split(" ")
        stacks.append(line)

# Remove the empty spaces in the stacks
for i in range(0, 9):
    for line in stacks:
        if line[i:i+4] == empty_space:
            line[i] = ""
            del line[i+1:i+4]

# print("The stacks are", stacks)

# Append the data to lists representing each stack
for line in stacks:
    stack_1.append(line[0])
    stack_2.append(line[1])
    stack_3.append(line[2])
    stack_4.append(line[3])
    stack_5.append(line[4])
    stack_6.append(line[5])
    stack_7.append(line[6])
    stack_8.append(line[7])
    stack_9.append(line[8])

# Remove the empty space within the stacks
for line in stacks:
    if "" in stack_1:
        stack_1.remove("")
    if "" in stack_2:
        stack_2.remove("")
    if "" in stack_3:
        stack_3.remove("")
    if "" in stack_4:
        stack_4.remove("")
    if "" in stack_5:
        stack_5.remove("")
    if "" in stack_6:
        stack_6.remove("")
    if "" in stack_7:
        stack_7.remove("")
    if "" in stack_8:
        stack_8.remove("")
    if "" in stack_9:
        stack_9.remove("")

# Create a list of the instructions
instructions = []

for line in data:
    if line[0:4] == "move":
        instructions.append(line)

# Create a list representing the numbers within the instructions
instructions_numbers = []
for item in instructions:
    for subitem in item.split():
        if (subitem.isdigit()):
            instructions_numbers.append(subitem)

len_instructions = len(instructions_numbers)
q_moved = 0
stack_reduced = 0
stack_increased = 0
item_moved = []

for i in range(0, len_instructions, 3):
    q_moved = int(instructions_numbers[i])
    stack_reduced = int(instructions_numbers[i+1])
    stack_gained = int(instructions_numbers[i+2])

# Remove items from stack_reduced
    for j in range(0, q_moved):
        if stack_reduced == 1:
            item_moved.append(stack_1[0])
            stack_1.pop(0)
        if stack_reduced == 2:
            item_moved.append(stack_2[0])
            stack_2.pop(0)
        if stack_reduced == 3:
            item_moved.append(stack_3[0])
            stack_3.pop(0)
        if stack_reduced == 4:
            item_moved.append(stack_4[0])
            stack_4.pop(0)
        if stack_reduced == 5:
            item_moved.append(stack_5[0])
            stack_5.pop(0)
        if stack_reduced == 6:
            item_moved.append(stack_6[0])
            stack_6.pop(0)
        if stack_reduced == 7:
            item_moved.append(stack_7[0])
            stack_7.pop(0)
        if stack_reduced == 8:
            item_moved.append(stack_8[0])
            stack_8.pop(0)
        if stack_reduced == 9:
            item_moved.append(stack_9[0])
            stack_9.pop(0)

    # print("Items moved are", item_moved)

    # Move items to stack gained
    if stack_gained == 1:
        stack_1 = item_moved + stack_1
    if stack_gained == 2:
        stack_2 = item_moved + stack_2
    if stack_gained == 3:
        stack_3 = item_moved + stack_3
    if stack_gained == 4:
        stack_4 = item_moved + stack_4
    if stack_gained == 5:
        stack_5 = item_moved + stack_5
    if stack_gained == 6:
        stack_6 = item_moved + stack_6
    if stack_gained == 7:
        stack_7 = item_moved + stack_7
    if stack_gained == 8:
        stack_8 = item_moved + stack_8
    if stack_gained == 9:
        stack_9 = item_moved + stack_9
    item_moved = []

print("Answer Day 5, Part 2 is", stack_1[0], stack_2[0], stack_3[0],
      stack_4[0], stack_5[0], stack_6[0], stack_7[0], stack_8[0], stack_9[0])
