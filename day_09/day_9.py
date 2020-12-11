def get_data(filename):
    f = open(filename, "r")
    data_list = [int(num) for num in f]
    return data_list

def sum_2(target, a_list):
    """
    Find the two numbers in a list that sum to a target number and return their product.
    Return None if no two numbers sum to the target number. O(n)
    """
    nums_found = {}
    for num in a_list:
        if num not in nums_found:
            nums_found[target - num] = num
            continue
        return True
    return None


def find_bad_num(preamble, data_list):
    """
    O(n^2)
    """
    curr_index = preamble
    for num in data_list[preamble - 1:]:
        my_list = data_list[curr_index - preamble:curr_index]

        if not sum_2(data_list[curr_index], my_list):
            return data_list[curr_index]
        curr_index += 1
    return None


def find_encryption_weakness(target, data_list):
    """
    O(n).
    """
    head_counter = 0
    tail_counter = 1

    my_sum = sum(data_list[head_counter:tail_counter + 1])
    while my_sum != target:
        if my_sum < target:
            tail_counter += 1
            my_sum += data_list[tail_counter]
        if my_sum > target:
            my_sum -= data_list[head_counter]
            head_counter += 1

    added_values = data_list[head_counter:tail_counter + 1]
    return max(added_values) + min(added_values)


a_list = get_data("input_day_9.txt")
broken_number = find_bad_num(5, a_list)
print(broken_number)  # Part 1 answer
print(find_encryption_weakness(broken_number, a_list))  # Part 2 answer
