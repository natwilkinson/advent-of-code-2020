# Advent of Code - Day 2

def get_valid_passwords(filename):
    """
    Finds valid password count using part 2 rules.
    """
    f = open(filename, "r")
    valid_passwords = 0

    for line in f:
        data = line.split()
        [min_num, max_num] = [int(x) - 1 for x in data[0].split("-")]

        if has_valid_password_part_2(min_num, max_num, data[1][0], data[2]):
            valid_passwords += 1

    return valid_passwords


def has_valid_password_part_1(min_num, max_num, target, password):
    """
    Determines the validity of a password for Part 1. A password is valid if the target
    character is in the password >= min_num and <= max_num.
    """
    target_count = 0

    for char in password:
        if char == target:
            target_count += 1
        if target_count > max_num:
            return False

    if target_count < min_num:
        return False
    return True


def has_valid_password_part_2(index_1, index_2, target, password):
    """
    Determines the validity of a password for Part 2. A password is valid if the target
    character is found at index_1 or index_2, but not both (exclusive or).
    """
    if (password[index_1] == target) is not (password[index_2] == target):
        return True
    return False
