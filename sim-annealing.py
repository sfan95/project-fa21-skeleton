# sim annealing with random restarts

from parse import read_input_file, write_output_file
import os
from igloovalue import eval_igloos
import random
import importlib  

baseline = importlib.import_module("greedly-earliest-deadline")

# hyperparameters
N_SWAPS = 4
SCHEDULED_DECREASED = 0.99

def solve(tasks):
    """
    Args:
        tasks: list[Task], list of igloos to polish
    Returns:
        output: list of igloos in order of polishing  
    """ 
    def get_rand_start():
        shuffled_tasks = list(tasks)
        random.shuffle(shuffled_tasks)
        start = []
        total_time = 0
        for task in shuffled_tasks:
            if total_time + task.get_duration() >= 1440:
                break
            start.append(task.get_task_id())
            total_time += task.get_duration()
        return start

    best_res, best_val = None, 0
    start = get_rand_start()
    res, res_val = sim_anneal(tasks, start)
    return res
    
def sim_anneal(tasks, start):
    tasks = list(tasks)
    tasks_to_do = list(start)
    p_accept_bad = 1
    while True:
        old_value, max_value = eval_igloos(tasks, tasks_to_do)
        new_tasks_to_do = list(tasks_to_do)
        for _ in range(N_SWAPS):
            # swap_val = random.uniform(0, 1)
            # if swap_val <= 0.4:
            i = random.randint(0, len(tasks_to_do) - 1)
            j = random.randint(0, len(tasks_to_do) - 1)
            new_tasks_to_do[i], new_tasks_to_do[j] = new_tasks_to_do[j], new_tasks_to_do[i]
            # elif swap_val <= 0.4:
            #     tasks_not_used = [task for task in tasks if task.get_task_id() not in tasks_to_do]
            #     i = random.randint(0, len(tasks_to_do) - 1)
            #     new_tasks_to_do[i] = random.choice(tasks_not_used).get_task_id()
            # # else:
            #     tasks_not_used = [task for task in tasks if task.get_task_id() not in tasks_to_do]
            #     new_tasks_to_do.append(random.choice(tasks_not_used).get_task_id())
        # if is_valid(tasks, new_tasks_to_do):
        new_value, max_value = eval_igloos(tasks, new_tasks_to_do)
        accept_bad = random.uniform(0, 1)
        if new_value > old_value or accept_bad >= p_accept_bad:
            tasks_to_do = new_tasks_to_do
            p_accept_bad *= SCHEDULED_DECREASED
        else:
            return tasks_to_do, old_value

def is_valid(tasks, task_inds):
    return sum([tasks[i - 1].get_duration() for i in task_inds]) <= 1440

if __name__ == '__main__':
    for input_size in ['small/', 'medium/', 'large/']:
        for input_path in os.listdir('inputs/' + input_size):
            print(input_path)
            output_path = 'outputs/' + input_size + input_path[:-3] + '.out'
            if input_path[0] != '.':
                tasks = read_input_file('inputs/' + input_size + input_path)
                output = solve(tasks)
                write_output_file(output_path, output)
