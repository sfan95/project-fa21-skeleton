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
    tasks59 = [task for task in tasks if task.get_max_benefit() == 59]
    tasks59.sort(key=lambda task: task.get_deadline())
    time = 0
    tasks_to_do = []
    i = 0
    while time < 1440:
        if time >= tasks59[i].get_deadline():
            i += 1
            continue
        tasks_to_do.append(tasks59[i].get_task_id())
        time += 30
        i += 1
    print(tasks_to_do)
    return tasks_to_do

if __name__ == '__main__':
    tasks = read_input_file('inputs/small/small-74.in')
    output = solve(tasks)
    write_output_file("outputs/small/small-74.out", output)
    print(eval_igloos(tasks, output))
