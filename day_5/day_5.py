# Advent of Code - Day 5

def get_number_valid_ids(filename):
    f = open(filename).read()
    ids = f.split("\n\n")
    total_valid = 0

    for id_data in ids:
        id_codes_and_data = id_data.split()

        # Create a dict of codes and values for a person's id
        code_val_dict = {}
        for code_and_data in id_codes_and_data:
            split_item = code_and_data.split(":")
            code_val_dict[split_item[0]] = split_item[1]

        total_valid += 1 if valid_id_data(code_val_dict) else 0

    return total_valid

# print(get_number_valid_ids("input_day_4.txt"))


def calculate_row(sequence):
    curr_min = 0
    curr_max = 127
    for char in sequence:
        # print(char)
        half = round((curr_max - curr_min) / 2)
        if char == "F":
            curr_max = curr_min + half
            # print((curr_min, curr_max))
        elif char == "B":
            curr_min = curr_min + half
            # print((curr_min, curr_max))
    # print(curr_min)
    # print(curr_max)
    return min(curr_max, curr_min)


def calculate_column(sequence):
    curr_min = 0
    curr_max = 7
    for char in sequence:
        # print(char)
        half = (curr_max - curr_min) // 2
        if char == "L":
            curr_max = curr_min + half
            # print((curr_min, curr_max))
        elif char == "R":
            curr_min = curr_min + half
            # print((curr_min, curr_max))
    # print(curr_min)
    # print(curr_max)
    return max(curr_max, curr_min)


def calc_totals(filename):
    f = open(filename).readlines()
    # print(f)
    total_max = 0
    totals = []
    for line in f:
        line = line.strip()
        row = line[:7]
        column = line[-3:]
        product = calculate_row(row) * 8 + calculate_column(column)
        # if product > total_max:
        #     total_max = product
        totals.append(product)
    totals.sort()
    my_seat = find_missing(totals)

    return my_seat


def find_my_seat(seat_list):
    past = -1
    future = -1
    for i in range(len(seat_list)):
        curr = seat_list[i]

def find_missing(lst):
    return [x for x in range(lst[0], lst[-1]+1)
                               if x not in lst]


def calc(sequence):
    row = sequence[:7]
    column = sequence[-3:]
    product = calculate_row(row) * 8 + calculate_column(column)
    return product

# print(calculate_row("FBFBBFF"))

# print(calculate_column("RLR"))
print(calc_totals("input_day_5.txt"))
# print(calc("BBFFBBFRLL"))

# 6328