def get_data(filename):
    """
    ASDF
    """
    f = open(filename).readlines()
    operations = {}

    for i,line in enumerate(f):
        line_list = line.split()
        operations[i] = (line_list[0], int(line_list[1]))

    return operations


def run_program(operations_dict, curr_index, accumulator, visited_ind):
    # program terminates and returns accumulator at the end
    if curr_index not in operations_dict:
        return accumulator

    action, change = operations_dict[curr_index]

    if curr_index not in visited_ind:
        visited_ind.add(curr_index)
    else:
        return None  # terminate if program loops

    # perform updates based on action type
    if action == "nop":
        curr_index += 1
    if action == "acc":
        accumulator = accumulator + change
        curr_index += 1
    if action == "jmp":
        curr_index += change

    # re-run program until it terminates
    return run_program(operations_dict, curr_index, accumulator, visited_ind)


def try_alternatives(operations):
    for key in operations:
        action, change = operations[key]

        if action == "acc":
            continue
        if action == "nop":
            copy = operations.copy()
            copy[key] = ["jmp", change]
            value = run_program(copy, 0, 0, set())
            if value:
                return value
        if action == "jmp":
            copy = operations.copy()
            copy[key] = ["nop", change]
            value = run_program(copy, 0, 0, set())
            if value:
                return value
    return None