# Read input
with open("Advent of Code Day 6 - Input.txt", "r") as my_file:
    data = my_file.read().strip().split()

# print(data)

my_string = data[0]

# Iterate over the length of the string
# At each position check if the next eight characters can be a part of a set. A set can't have duplicates so when the if statement is true we have found the answer.
# Return the current index + 4 since we need the end of the 4-character sequence
for i in range(len(my_string)):
    if len(set(my_string[i:i+8])) == 8:
        print("Answer Day 6, Part 1 is", i+4)
        break

#--------------------------------------------------------------------#

# Same solution as above but the length of the string checked is now 14
for i in range(len(my_string)):
    if len(set(my_string[i:i+14])) == 14:
        print("Answer Day 6, Part 2 is", i+14)
        break
