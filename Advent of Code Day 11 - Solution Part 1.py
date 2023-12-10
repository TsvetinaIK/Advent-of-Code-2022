with open("Advent of Code Day 11 - Input.txt") as my_file:
    data = my_file.read().strip().split("\n\n")

# print(data)
block = [block.split("\n") for block in data]

monkeys = []

def conduct_operation(operation, x):
    if operation[0] == "+":
        return x + int(operation[2:])
    else:
        if operation[-3:] == "old":
            return x * x
        else:
            return x * int(operation[2:])

class Monkey:
    def __init__(self, monkey_number, items, operation, test):
        self.monkey_number = monkey_number
        self.items = items
        self.operation = operation
        self.test = test
        self.inspections = 0

    def __str__(self):
        return f"{self.items}, {self.operation}, {self.test}"


for lst in block:
    monkey_number = int(lst[0][7])
    items = list(map(int, lst[1].strip("  Starting items: ").split(", ")))
    operation = lst[2][23:]
    # print(operation)
    mod = int(lst[3].strip("  Test: divisible by "))
    if_true = int(lst[4].strip("    If true: throw to monkey "))
    if_false = int(lst[5].strip("    If false: throw to monkey "))

    # We turn it all to a monkey object which accepts items, operation, etc.
    monkeys.append(Monkey(
        monkey_number,
        items,
        operation,
        [mod, if_true, if_false]
    ))


# Do the rounds
n_of_monkeys = len(monkeys)

for round in range(20):
    for i in range(n_of_monkeys):
        monkey = monkeys[i]
        for item in monkey.items:
            # item is an int, representing worry level
            item = conduct_operation(monkey.operation, item)
            item //= 3

            mod, if_true, if_false = monkey.test

            if item % mod == 0:
                monkeys[if_true].items.append(item)
            else:
                monkeys[if_false].items.append(item)

            monkey.inspections += 1

        # Empty the list of items
        monkey.items = []

amounts = [m.inspections for m in monkeys]
sorted_amts = sorted(amounts)
print("Answer Day 11, Part 1 is", sorted_amts[-1] * sorted_amts[-2])