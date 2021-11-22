# start with random order
# swap out NSWAP values and take the new order if its is valid + better
# wp 0.5: swap curr task orderings
# wp 0.5: swap for task not in the ordering
# wp ...: append a new task

from parse import read_input_file, write_output_file
import os
from igloovalue import eval_igloos
import random
import importlib  

baseline = importlib.import_module("greedly-earliest-deadline")

# hyperparameters
N_SWAPS = 3

def solve(tasks):
    """
    Args:
        tasks: list[Task], list of igloos to polish
    Returns:
        output: list of igloos in order of polishing  
    """ 
    tasks = list(tasks)
    random.shuffle(tasks)
    start = []
    total_time = 0
    for task in tasks:
        if total_time + task.get_duration() >= 1440:
            break
        start.append(task.get_task_id())
        total_time += task.get_duration()
    print(total_time)
    return local_search(tasks, start)
    
def local_search(tasks, start):
    tasks = list(tasks)
    temp = 1
    tasks_to_do = start
    while True:
        old_value, max_value = eval_igloos(tasks, tasks_to_do)
        new_tasks_to_do = list(tasks_to_do)
        for _ in range(N_SWAPS):
            swap_val = random.uniform(0, 1)
            if swap_val <= 0.4:
                i = random.randint(0, len(tasks_to_do) - 1)
                j = random.randint(0, len(tasks_to_do) - 1)
                new_tasks_to_do[i], new_tasks_to_do[j] = tasks_to_do[j], tasks_to_do[i]
            elif swap_val <= 0.4:
                tasks_not_used = [task for task in tasks if task.get_task_id() not in tasks_to_do]
                i = random.randint(0, len(tasks_to_do) - 1)
                new_tasks_to_do[i] = random.choice(tasks_not_used).get_task_id()
            else:
                tasks_not_used = [task for task in tasks if task.get_task_id() not in tasks_to_do]
                new_tasks_to_do.append(random.choice(tasks_not_used).get_task_id())
        if is_valid(tasks, new_tasks_to_do):
            accept_bad = random.uniform(0, 1)
            new_value, max_value = eval_igloos(tasks, new_tasks_to_do)
            if new_value >= old_value or accept_bad <= temp:
                tasks_to_do = new_tasks_to_do
            else:
                return tasks_to_do
        temp *= 0.99

def is_valid(tasks, task_inds):
    return sum([tasks[i - 1].get_duration() for i in task_inds]) <= 1440

if __name__ == '__main__':
    for input_path in os.listdir('inputs/'):
        output_path = 'outputs/' + input_path[:-3] + '.out'
        tasks = read_input_file('inputs/' + input_path)
        output = solve(tasks)
        write_output_file(output_path, output)
        print(eval_igloos(tasks, output))