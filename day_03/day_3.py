# Advent of Code - Day 3

def number_of_trees_hit(ski_map, slope):
    """
    Calculates the number of trees hit given a map and a specific slope. O(n) where n is
    len(ski_map) // y_move. Worst case n = len(ski_map).
    """
    curr_x, num_trees = (0, 0)
    x_move, y_move = slope

    for i in range(0, len(ski_map), y_move):
        position = ski_map[i]

        if position[curr_x] == "#":  # if hits tree
            num_trees += 1

        curr_x = (curr_x + x_move) % 31

    return num_trees


def multi_slope_tree_hit_product(slope_list, filename):
    """
    Calculates the product of all of the trees hit for a list of slopes. O(kn) where k is
    the number of slopes you want to calculate.
    """
    f = open(filename).read().splitlines()

    product = 1
    for slope in slope_list:
        product *= number_of_trees_hit(f, slope)

    return product


slope_list = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2),
]
print(multi_slope_tree_hit_product(slope_list, "input_day_3.txt"))
