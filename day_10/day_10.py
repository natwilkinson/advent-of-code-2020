from collections import defaultdict


def get_data(filename):
    f = open(filename, "r")
    data_list = [int(num) for num in f]
    return sorted(data_list)


def calculate_jolts(data_list):
    d1, d3 = (0, 1)  # diff_3 = 1 b/c we count device joltage
    t = 0
    for num in data_list:
        d = num - t
        if d == 1:
            d1 += 1
        elif d == 3:
            d3 += 1
        t += d
    return d1 * d3


def all_possible_combos(data_list):
    """Bottom to Top build tree"""
    found = defaultdict(int)
    found[0] = 1

    for num in data_list:
        found[num] = found[num - 3] + found[num - 2] + found[num - 1]
    return found[num]


# Solutions:
data_list = get_data("input_day_10.txt")

print(calculate_jolts(data_list))  # Part 1 Solution
print(all_possible_combos(data_list))  # Part 2 Solution