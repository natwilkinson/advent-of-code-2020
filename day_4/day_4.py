# Advent of Code - Day 4

def byr_is_valid(val):
    if len(val) != 4 or int(val) > 2002 or int(val) < 1920:
        return False
    return True

def iyr_is_valid(val):
    if len(val) != 4 or int(val) > 2020 or int(val) < 2010:
        return False
    return True

def eyr_is_valid(val):
    if len(val) != 4 or int(val) > 2030 or int(val) < 2020:
        return False
    return True

def hgt_is_valid(val):
    if "cm" in val:
        num = int(val[:-2])
        if num > 193 or num < 150:
            return False
    elif "in" in val:
        num = int(val[:-2])
        if num > 76 or num < 59:
            return False
    else:
        return False
    return True


def hcl_is_valid(val):
    if val[0] != "#":
        return False
    if len(val[1:]) != 6:
        return False
    for char in val[1:]:
        if char.isdigit() or char.isalpha():
            continue
        else:
            return False
    return True


def ecl_is_valid(val):
    eye_set = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
    if val not in eye_set:
        return False
    return True


def pid_is_valid(val):
    if len(val) != 9 or not val.isdigit():
        return False
    return True


def valid_id_data(code_val_dict):
    required_codes = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    valid = True
    for code in required_codes:
        if code not in code_val_dict: valid = False; break

        val = code_val_dict[code]

        if code == "byr" and not byr_is_valid(val): valid = False; break

        if code == "iyr" and not iyr_is_valid(val): valid = False; break

        if code == "eyr" and not eyr_is_valid(val): valid = False; break

        if code == "hgt" and not hgt_is_valid(val): valid = False; break

        if code == "hcl" and not hcl_is_valid(val): valid = False; break

        if code == "ecl" and not ecl_is_valid(val): valid = False; break

        if code == "pid" and not pid_is_valid(val): valid = False; break

    return valid

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

print(get_number_valid_ids("input_day_4.txt"))