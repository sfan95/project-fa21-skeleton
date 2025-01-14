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
    highest_profit_tasks = highest_profit_decay.solve(tasks)
    earliest_deadline_tasks = earliest_deaadline.solve(tasks)
    # random_strategy_tasks = random_greedy.solve(tasks)
    # return max([highest_profit_tasks] + random_strategy_tasks, key=lambda tasks_to_do: eval_igloos(tasks, tasks_to_do)[0])
    return max(highest_profit_tasks, earliest_deadline_tasks, key=lambda tasks_to_do: eval_igloos(tasks, tasks_to_do)[0])

total = 0
if __name__ == '__main__':
    # for input_size in ['small/', 'medium/', 'large/']:
    #     for input_path in os.listdir('inputs/' + input_size):
    #         output_path = 'outputs/' + input_size + input_path[:-3] + '.out'
    #         if input_path[0] != '.':
    #             tasks = read_input_file('inputs/' + input_size + input_path)
    #             output = solve(tasks)
    #             write_output_file(output_path, output)
    #             total += eval_igloos(tasks, output)[0]
    # print(total)
    # tasks = read_input_file('inputs/large/large-202.in')
    # output = solve(tasks)
    # write_output_file("outputs/large/large-202.in", output)
    # print(output)
    tasks = read_input_file('inputs/small/small-235.in')
    output = solve(tasks)
    write_output_file("outputs/small/small-235.in", output)
    # print([1] + output[:-1])
    print(eval_igloos(tasks, [1] + list(range(52, 100)) + [50]))