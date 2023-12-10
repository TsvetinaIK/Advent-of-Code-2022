# Read input
with open("Advent of Code Day 4 - Input.txt", "r") as my_file:
    lines = my_file.read().strip().split("\n")

# print(lines)

# Create a new list with sections of assignment pairs by splitting the data according to ","
# Split the pairs within the sections by splitting the data according to "-"

l_of_sections = []

for line in lines:
    line = line.split(",")
    for pairs in line:
        pairs = pairs.split("-")
        l_of_sections.append(pairs)

# print(l_of_sections)

# Compare the numbers within each section
len_l_of_sections = len(l_of_sections)
n_of_pairs = int(len(l_of_sections)/2)

n_of_pairs_counted_round1 = 0
n_of_pairs_counted_round2 = 0

n_to_compare_1 = 0
n_to_compare_2 = 0
n_to_compare_3 = 0
n_to_compare_4 = 0

# Some of the pairs will be counted twice so we need to subtract that number from the total
n_counted_twice = 0

for i in range(0, len_l_of_sections, 2):
    n_to_compare_1 = int(l_of_sections[0 + i][0])
    n_to_compare_2 = int(l_of_sections[0 + i][1])
    n_to_compare_3 = int(l_of_sections[1 + i][0])
    n_to_compare_4 = int(l_of_sections[1 + i][1])

    if n_to_compare_1 in range(n_to_compare_3, n_to_compare_4+1):
        if n_to_compare_2 in range(n_to_compare_3, n_to_compare_4+1):
            n_of_pairs_counted_round1 += 1

    if n_to_compare_3 in range(n_to_compare_1, n_to_compare_2+1):
        if n_to_compare_4 in range(n_to_compare_1, n_to_compare_2+1):
            n_of_pairs_counted_round2 += 1

    if n_to_compare_1 == n_to_compare_3 and n_to_compare_2 == n_to_compare_4:
        n_counted_twice += 1

# print("Counted twice:", n_counted_twice)

print("Answer Day 4, Part 1 is", n_of_pairs_counted_round1+n_of_pairs_counted_round2-n_counted_twice,
      "which is the total number of pairs for which one pair fully contains the other.")

#----------------------------------------------------------------------------------------#

# The number of pairs that are at least partially overlapping
n_of_pairs_counted_round3 = 0
n_of_pairs_counted_round4 = 0

n_to_compare_1 = 0
n_to_compare_2 = 0
n_to_compare_3 = 0
n_to_compare_4 = 0

for i in range(0, len_l_of_sections, 2):
    n_to_compare_1 = int(l_of_sections[0 + i][0])
    n_to_compare_2 = int(l_of_sections[0 + i][1])
    n_to_compare_3 = int(l_of_sections[1 + i][0])
    n_to_compare_4 = int(l_of_sections[1 + i][1])

    if n_to_compare_1 in range(n_to_compare_3, n_to_compare_4+1) or n_to_compare_2 in range(n_to_compare_3, n_to_compare_4+1) or n_to_compare_3 in range(n_to_compare_1, n_to_compare_2+1) or n_to_compare_4 in range(n_to_compare_1, n_to_compare_2+1):
        n_of_pairs_counted_round3 += 1

print("Answer Day 4, Part 2 is", n_of_pairs_counted_round3,
      "which is the total number of pairs that are at least partially overlapping.")
