from parse import read_input_file, write_output_file
import os
from igloovalue import eval_igloos
from itertools import permutations
from functools import lru_cache
import importlib

highest_profit_decay = importlib.import_module("greedy-with-decay")
random_greedy = importlib.import_module("random_greedy")
earliest_deaadline = importlib.import_module("greedly-earliest-deadline")

def solve(tasks):
    """
    Args:
        tasks: list[Task], list of igloos to polish
    Returns:
        output: list of igloos in order of polishing  
    """
    return earliest_deaadline.solve(tasks)

if __name__ == '__main__':
    tasks = read_input_file('inputs/small/small-112.in')
    output = solve(tasks)
    write_output_file("outputs/small/small-112.out", output)
    print(eval_igloos(tasks, output))
