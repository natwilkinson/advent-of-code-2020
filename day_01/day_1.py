# Advent of Code - Day 1

def sum_2(target, a_list):
    """
    Find the two numbers in a list that sum to a target number and return their product.
    Return None if no two numbers sum to the target number.
    """
    expenses_found = {}

    for expense in a_list:
        if expense not in expenses_found:
            expenses_found[target - expense] = expense
            continue
        return expenses_found[expense] * expense
    return None


def sum_3(target, a_list):
    """
    Find the product of three numbers in a list that sum to the target number. Returns None
    if no three numbers sum to the target number.
    """
    for i, expense in enumerate(a_list):
        left_over = 2020 - expense

        x = sum_2(left_over, a_list[:i] + a_list[i+1:])
        if x:
            return x * expense

    return None


def get_total_expenses(filename):
    """
    Calculates the total expenses for vacation in 2020.
    """
    f = open(filename, "r")
    expense_list = [int(ex) for ex in f]

    return sum_3(2020, expense_list)
