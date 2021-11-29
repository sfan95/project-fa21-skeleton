from parse import read_input_file, write_output_file
import os
from igloovalue import eval_igloos
from itertools import permutations
from functools import lru_cache
import importlib

highest_profit_decay = importlib.import_module("greedy-with-decay")
random_greedy = importlib.import_module("random_greedy")

def solve(tasks):
    """
    Args:
        tasks: list[Task], list of igloos to polish
    Returns:
        output: list of igloos in order of polishing  
    """
    highest_profit_tasks = highest_profit_decay.solve(tasks)
    random_strategy_tasks = [random_greedy.solve(tasks) for x in range(30)]
    return max([highest_profit_tasks] + random_strategy_tasks, key=lambda tasks_to_do: eval_igloos(tasks, tasks_to_do)[0])

if __name__ == '__main__':
    for input_size in ['small/', 'medium/', 'large/']:
        for input_path in os.listdir('inputs/' + input_size):
            output_path = 'outputs/' + input_size + input_path[:-3] + '.out'
            if input_path[0] != '.':
                tasks = read_input_file('inputs/' + input_size + input_path)
                output = solve(tasks)
<<<<<<< HEAD
                write_output_file(output_path, output)
=======
                write_output_file(output_path, output)
>>>>>>> 319e6a0dd838f4c011751a594e43cbefd1787a6a
