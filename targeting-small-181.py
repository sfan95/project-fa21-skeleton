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
    time = 0
    tasks_to_do = []
    tasks = list(tasks)
    tasks.sort(key=lambda task: -task.get_max_benefit() / task.get_duration())
    i = 0
    while time < 1440 and i < len(tasks):
        if tasks[i].get_duration() + time <= 1440:
            tasks_to_do.append(tasks[i].get_task_id())
            time += tasks[i].get_duration()
            print("put", tasks[i].get_task_id(), tasks[i].get_duration(), tasks[i].get_max_benefit())
        else:
            print("skipped", tasks[i].get_task_id(), tasks[i].get_duration(), tasks[i].get_max_benefit())
        i += 1
    return tasks_to_do

if __name__ == '__main__':
    tasks = read_input_file('inputs/small/small-181.in')
    output = solve(tasks)
    write_output_file("outputs/small/small-181.out", output)
    print(eval_igloos(tasks, output))
