# Read input
with open("Advent of Code Day 3 - Input.txt", "r") as my_file:
    lines = my_file.read().strip().split("\n")

# print(lines)

# Break the lines into different compartments and find the characters
l_of_items = []

for line in lines:
    length = int(len(line))
    index = int(length/2)
    compartment1 = line[:index]
    compartment2 = line[index:]
    for char in compartment1:
        if char in compartment2:
            l_of_items.append(char)
            break
            # break the loop to avoid counting the character multiple times

# print(l_of_items)

# Find the priority of the item type by calculating the index of its position in a string
priority_total = 0
priority_of_char = 0
my_string = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
l_of_piority = []

for char in l_of_items:
    if char in my_string:
        priority_of_char = my_string.index(char) + 1
        l_of_piority.append(priority_of_char)
        priority_total += priority_of_char

print("Answer Day 3, Part 1 is", priority_total)

#----------------------------------------------------------------------------------------#

# Separate the groups in sets of 3
# Find the item type that appear in all three rucksacks within a set
n_of_rucksacks = len(lines)
n_of_sets_of_3 = int(n_of_rucksacks/3)
set_of_3_lines = []
l_of_items2 = []

for i in range(0, n_of_rucksacks, 3):
    for char in lines[(n_of_rucksacks-i-1)]:
        if char in lines[(n_of_rucksacks-i-2)]:
            if char in lines[(n_of_rucksacks-i-3)]:
                l_of_items2.append(char)
                break

priority_total2 = 0

# Find the priority of the item type by calculating the index of its position in a string
for char in l_of_items2:
    if char in my_string:
        priority_of_char = my_string.index(char) + 1
        l_of_piority.append(priority_of_char)
        priority_total2 += priority_of_char

print("Answer Day 3, Part 2 is", priority_total2)
