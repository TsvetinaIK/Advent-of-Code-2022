# Read input
with open("Advent of Code Day 6 - Input.txt", "r") as my_file:
    data = my_file.read().strip().split()

# print(data)

my_string = data[0]
len_of_string = len(my_string)

# Iterate through the characters in the string and add them to the list of characters to be checked
# Compare each character to the characters in the list and continue only if there is no match
# If the iteration is not successful, empty the list and start again with the next set of characters

l_of_char_to_be_checked = []

for i in range(len_of_string-7):
    l_of_char_to_be_checked.append(my_string[i])
    if my_string[i+1] not in l_of_char_to_be_checked:
        l_of_char_to_be_checked.append(my_string[i+1])
        if my_string[i+2] not in l_of_char_to_be_checked:
            l_of_char_to_be_checked.append(my_string[i+2])
            if my_string[i+3] not in l_of_char_to_be_checked:
                l_of_char_to_be_checked.append(my_string[i+3])
                if my_string[i+4] not in l_of_char_to_be_checked:
                    l_of_char_to_be_checked.append(my_string[i+4])
                    if my_string[i+5] not in l_of_char_to_be_checked:
                        l_of_char_to_be_checked.append(my_string[i+5])
                        if my_string[i+6] not in l_of_char_to_be_checked:
                            l_of_char_to_be_checked.append(my_string[i+6])
                            if my_string[i+7] not in l_of_char_to_be_checked:
                                l_of_char_to_be_checked.append(my_string[i+7])
                                print("Answer Day 6, Part 1 is", i+4)
                                break
    l_of_char_to_be_checked = []

#--------------------------------------------------------------------#

# Same solution as above but the length of the string checked is now 14

l_of_char_to_be_checked = []

for i in range(len_of_string-14):
    l_of_char_to_be_checked.append(my_string[i])
    if my_string[i+1] not in l_of_char_to_be_checked:
        l_of_char_to_be_checked.append(my_string[i+1])
        if my_string[i+2] not in l_of_char_to_be_checked:
            l_of_char_to_be_checked.append(my_string[i+2])
            if my_string[i+3] not in l_of_char_to_be_checked:
                l_of_char_to_be_checked.append(my_string[i+3])
                if my_string[i+4] not in l_of_char_to_be_checked:
                    l_of_char_to_be_checked.append(my_string[i+4])
                    if my_string[i+5] not in l_of_char_to_be_checked:
                        l_of_char_to_be_checked.append(my_string[i+5])
                        if my_string[i+6] not in l_of_char_to_be_checked:
                            l_of_char_to_be_checked.append(my_string[i+6])
                            if my_string[i+7] not in l_of_char_to_be_checked:
                                l_of_char_to_be_checked.append(my_string[i+7])
                                if my_string[i+8] not in l_of_char_to_be_checked:
                                    l_of_char_to_be_checked.append(
                                        my_string[i+8])
                                    if my_string[i+9] not in l_of_char_to_be_checked:
                                        l_of_char_to_be_checked.append(
                                            my_string[i+9])
                                        if my_string[i+10] not in l_of_char_to_be_checked:
                                            l_of_char_to_be_checked.append(
                                                my_string[i+10])
                                            if my_string[i+11] not in l_of_char_to_be_checked:
                                                l_of_char_to_be_checked.append(
                                                    my_string[i+11])
                                                if my_string[i+12] not in l_of_char_to_be_checked:
                                                    l_of_char_to_be_checked.append(
                                                        my_string[i+12])
                                                    if my_string[i+13] not in l_of_char_to_be_checked:
                                                        l_of_char_to_be_checked.append(
                                                            my_string[i+13])
                                                        print(
                                                            "Answer Day 6, Part 2 is", i+14)
                                                        break
    l_of_char_to_be_checked = []
