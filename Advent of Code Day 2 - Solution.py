# Read input
with open("Advent of Code Day 2 - Input.txt", "r") as my_file:
    lines = my_file.read().strip().split("\n")

# print(lines)

# Convert input to a list of two values which represent the two choices for each game played
l_of_lines = []

for line in lines:
    line = line.split(" ")
    l_of_lines.append(line)

# print(l_of_lines)

# Calculate score due to the shape
score1 = 0

for list in l_of_lines:
    if list[1] == 'X':
        score1 += 1
    if list[1] == 'Y':
        score1 += 2
    if list[1] == 'Z':
        score1 += 3

# print(score1)

# Calculate score due to outcome of the game
score2 = 0

for list in l_of_lines:
    # Draw rock
    if list[0] == 'A' and list[1] == 'X':
        score2 += 3
    # Draw paper
    if list[0] == 'B' and list[1] == 'Y':
        score2 += 3
    # Draw scissors
    if list[0] == 'C' and list[1] == 'Z':
        score2 += 3
    # Player 1: rock, Player 2: paper
    if list[0] == 'A' and list[1] == 'Y':
        score2 += 6
    # Player 1: paper, Player 2: scissors
    if list[0] == 'B' and list[1] == 'Z':
        score2 += 6
    # Player 1: scissors, Player 2: rock
    if list[0] == 'C' and list[1] == 'X':
        score2 += 6

# print(score2)

print("Answer Day 1, Part 1 is total score of", score1+score2)

#---------------------------------------------------------------------------#

# Calculate score due to the shape
score3 = 0

for list in l_of_lines:
    # If the round ends in a draw we win the same points for the shape as the opponent
    if list[1] == "Y":
        if list[0] == "A":
            score3 += 1
        if list[0] == "B":
            score3 += 2
        if list[0] == "C":
            score3 += 3

    # If we lose we need to determine which shape we played
    if list[1] == "X":
        if list[0] == "A":
            # If we lost because the opponent played rock that means we played scissors so we should get 3 points for the shape
            score3 += 3
        if list[0] == "B":
            # If we lost because the opponent played paper that means we played rock so we should get 1 point for the shape
            score3 += 1
        if list[0] == "C":
            # If we lost because the opponent played scissors that means we played paper so we should get 2 points for the shape
            score3 += 2

    # If we win we need to determine which shape we played
    if list[1] == "Z":
        if list[0] == "A":
            # If we won because the opponent played rock that means we played paper so we should get 2 points for the shape
            score3 += 2
        if list[0] == "B":
            # If we won because the opponent played paper that means we played scissors so we should get 3 points for the shape
            score3 += 3
        if list[0] == "C":
            # If we won because the opponent played scissors that means we played rock so we should get 1 point for the shape
            score3 += 1


# print(score3)

# Calculate score due to outcome of the game
score4 = 0

for list in l_of_lines:
    if list[1] == "Y":
        score4 += 3
    if list[1] == "Z":
        score4 += 6

# print(score4)

print("Answer Day 1, Part 2 is total score of", score3+score4)
