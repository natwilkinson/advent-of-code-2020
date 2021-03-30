# Advent of Code - Day 6


def get_groups(filename):
    f = open(filename).read()
    groups = f.split("\n\n")
    total_valid = 0

    for group in groups:
        total = get_yes_answers_for_group(group)
        # print(total)
        total_valid += total


    return total_valid

def get_yes_answers_for_group(group):
    person_list = group.split()
    # print(person_list)
    # answered_set = set()
    answered_set = {}

    for person in person_list:
        for char in person:
            if char not in answered_set:
                # answered_set.add(char)
                answered_set[char] = 1
            else:
                answered_set[char] += 1
    total = 0
    for char in answered_set:
        if answered_set[char] == len(person_list):
            total += 1
    return total

print(get_groups("input_day_6.txt"))