# Advent of Code - Day 3

def number_of_trees_hit(ski_map, x_move, y_move):
    """
    Calculates the number of trees hit given a map and a specific slope. O(n)
    """
    curr_x, num_trees = (0, 0)
    for i in range(0, len(ski_map), y_move):
        position = ski_map[i]
        if hits_tree(position, curr_x):
            num_trees += 1

        curr_x = (curr_x + x_move) % 31

    return num_trees


def hits_tree(position, x):
    """
    Returns boolean. True if a tree is hit, False if not. O(1)
    """
    return position[x] == "#"


def multi_slope_tree_hit_product(slope_list, filename):
    """
    Calculates the product of all of the trees hit for a list of slopes. O(kn) where k is
    the number of slopes you want to calculate.
    """
    f = open(filename).read().splitlines()

    product = 1
    for x, y in slope_list:
        product *= number_of_trees_hit(f, x, y)

    return product