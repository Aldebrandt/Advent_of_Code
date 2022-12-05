from day5_data import moves, stack_of_crates
import re

move_instructions = [[int(i) for i in re.findall(r"\b\d+\b", move)] for move in moves.split("\n")]

for i in range(len(move_instructions)):
    for j in range(move_instructions[i][0]):
        stack_of_crates[move_instructions[i][2] - 1].append(stack_of_crates[move_instructions[i][1] - 1][-1])
        stack_of_crates[move_instructions[i][1] - 1] = stack_of_crates[move_instructions[i][1] - 1][:-1]

final_crates = [stack[-1] for stack in stack_of_crates if len(stack) > 0]
print(final_crates)  # ['B', 'S', 'D', 'M', 'Q', 'F', 'L', 'S', 'P']
