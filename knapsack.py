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
    n = len(tasks)
    tasks = list(tasks)

    memo = {}
    for i in range(n + 1):
        for w in range(1441):
            if i == 0 or w == 0:
                memo[(i, w)] = 0
            elif tasks[i - 1].get_duration() <= w:
                memo[(i, w)] = max(memo[(i - 1, w)], tasks[i - 1].get_max_benefit() + memo[(i - 1, w - tasks[i - 1].get_duration())])
            else:
                memo[(i, w)] = memo[(i - 1, w)]

    res = memo[(n, 1440)]
    w = 1440
    tasks_to_do = []
    for i in range(n, 0, -1):
        if (res == memo[(i - 1, w)]):
            continue
        else:
            tasks_to_do.append(i)
            res -= tasks[i - 1].get_max_benefit()
            w -= tasks[i - 1].get_duration()

    return tasks_to_do


input_files = ['inputs/small/small-181.in', 'inputs/medium/medium-181.in', 'inputs/large/large-181.in', 'inputs/small/small-172.in']
if __name__ == '__main__':
    for input_file in input_files:
        tasks = read_input_file(input_file)
        output = solve(tasks)
        write_output_file("outputs" + input_file[6:-3] + ".out", output)
        print(eval_igloos(tasks, output))
