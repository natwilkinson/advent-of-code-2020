import re


def get_parent_bags_data(filename):
    """
    Data structure representing parent bags for each bag.
    {small bag: [parent bags, ..., ...]}
    """
    f = open(filename).readlines()

    bag_structure = {}
    for line in f:
        first_two_words = line.split()[:2]
        big_bag = f"{first_two_words[0]} {first_two_words[1]}"
        small_bags = re.findall(r"(?<=[0-9] )(.*?)(?= bag)", line)

        for bag in small_bags:
            if bag not in bag_structure:
                bag_structure[bag] = [big_bag]
            else:
                bag_structure[bag].append(big_bag)
    return bag_structure


def find_suitable_bags(target, bag_data, visited):
    """
    Returns total number of bag colors that will contain the target bag color.

    Attributes:
        target      String representing a bag to perform calculation on.
        bag_data    Dictionary representing a small bag (key) and a list of big bags nested
                    inside (value). Formatted by `get_parent_bags_data`.
        visited     Set of bags that calculation has already been performed on.
    """
    curr_sum = 0
    visited.add(target)
    if target not in bag_data:
        return 0

    for big_bag in bag_data[target]:
        if big_bag not in visited:
            curr_sum += find_suitable_bags(big_bag, bag_data, visited) + 1
    return curr_sum


def get_nested_bags_data(filename):
    """
    Data structure representing nested bags. { big bag: [(num nested bags, bag color), ...] }
    """
    f = open(filename).readlines()

    bag_structure = {}
    for line in f:
        first_two_words = line.split()[:2]
        big_bag = f"{first_two_words[0]} {first_two_words[1]}"

        # list of tuples. Ex: [('2', 'olive green'),...]
        small_bags = re.findall(r"(?=[0-9])(.*?).(?<=[0-9] )(.*?)(?= bag)", line)
        bag_structure[big_bag] = small_bags

    return bag_structure


def num_bags_inside(target, bag_data, visited):
    """
    Returns the total number of bags inside the target bag.

    Attributes:
        target      String representing a bag to perform calculation on.
        bag_data    Dictionary representing a big bag (key) and a list of small bags nested
                    inside (value). Formatted by `get_nested_bags_data`.
        visited     Dictionary of bags that calculation has already been performed on.
    """
    curr_sum = 1

    for little_bag in bag_data[target]:
        num_bags, bag_color = little_bag
        if bag_color not in visited:
            num_bags_inside(bag_color, bag_data, visited)

        curr_sum += int(num_bags) * visited[bag_color]
    visited[target] = curr_sum  # store bag data to avoid duplicate calculation
    return curr_sum - 1


# bag_data = get_parent_bags_data("input_day_7.txt")
# print(find_suitable_bags("shiny gold", bag_data, set()))
# print(num_bags_inside("shiny gold", bag_data, {} ))