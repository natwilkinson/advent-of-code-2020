def get_data(filename):
    """
    { index: (action, change), ... }
    """
    f = open(filename).readlines()
    operations = {}

    for i,line in enumerate(f):
        line_list = line.split()
        operations[i] = (line_list[0], int(line_list[1]))

    return operations


def run_program(operations_dict, curr_index, accumulator, visited_ind):
    """
    Returns accumulator value when program terminates. If program enters infinite loop,
    return None.
    """
    # program finishes and returns accumulator at end of file
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
    """
    Swaps "nop" and "jmp" actions and runs `run_program`. Returns accumulator value for
    program that successfully finishes. Returns None if no swapped solution exists.
    """
    for key in operations:
        action, change = operations[key]

        if action == "acc":
            continue

        swap_actions = { "jmp":"nop", "nop":"jmp" }
        operations[key] = (swap_actions[action], change)  # swap actions

        value = run_program(operations, 0, 0, set())
        if value:
            return value

        operations[key] = (action, change)  # swap actions back for next iteration
    return None