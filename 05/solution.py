import copy
from collections import deque
import os


def main():
    filename = "input"
    absolute_filepath = os.path.join(os.path.dirname(__file__), filename)

    # Read input
    with open(absolute_filepath) as file:
        lines = [line.rstrip() for line in file]

    # Parse the input instead of hardcoding it because we're epic >:)
    input = []
    for line in lines:
        if line.strip():
            input.append(line)
        else:
            break

    # last line: 1 2 3 ... 9, get the last number
    num_stacks = int(input[-1].strip(" ")[-1])

    # create a list of empty stacks (deques)
    stacks = []
    for _ in range(num_stacks):
        stacks.append(deque())
    for input_line in reversed(input[:-1]):
        for i in range(num_stacks):
            # symbol very 4 characters starting from the second
            # [S] [R] [Z] [V] [G] [R] [Q] [N] [Z]
            #  ^   ^   ^   ^   ^   ^   ^   ^   ^
            index = i * 4 + 1
            # if not empty, append to n-th stack
            if index <= len(input_line) and input_line[index] != ' ':
                stacks[i].append(input_line[index])

    # save this for later...
    stacks_copy = copy.deepcopy(stacks)

    # Rearrange the crates
    for line in lines[len(stacks)+1:]:
        commands = line.split(" ")
        # "move N from F to S"
        number, from_stack, to_stack = int(commands[1]), int(
            commands[3]) - 1, int(commands[5]) - 1
        # Rearrange N times from F to S
        for _ in range(number):
            crate = stacks[from_stack].pop()
            stacks[to_stack].append(crate)

    # Get the topmost crates
    result_1 = ""
    for stack in stacks:
        result_1 += stack[-1]
    print(result_1)

    # Rearrange the crates a bit differently
    for line in lines[len(stacks)+1:]:
        commands = line.split(" ")
        # "move N from F to S"
        number, from_stack, to_stack = int(commands[1]), int(
            commands[3]) - 1, int(commands[5]) - 1
        # Rearrange N times from F to S
        crates_to_move = []
        for _ in range(number):
            crates_to_move.append(stacks_copy[from_stack].pop())

        for crate in reversed(crates_to_move):
            stacks_copy[to_stack].append(crate)

    # Get the topmost crates
    result_2 = ""
    for stack in stacks_copy:
        result_2 += stack[-1]
    print(result_2)


if __name__ == "__main__":
    main()
