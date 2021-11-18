from parse import read_input_file, write_output_file
import os
from igloovalue import eval_igloos
from itertools import permutations

def solve(tasks):
    """
    Args:
        tasks: list[Task], list of igloos to polish
    Returns:
        output: list of igloos in order of polishing  
    """
    best_perm, best_val = [], 0
    for task_perm in permutations(tasks):
        perm_ids = [task.get_task_id() for task in task_perm]
        possible_val = eval_igloos(tasks, perm_ids)[0]
        if possible_val > best_val and is_valid(task_perm):
            best_val = possible_val
            best_perm = perm_ids
    print(best_perm)
    return best_perm

def is_valid(tasks):
    prev_time = -1
    time = 0
    for task in tasks:
        if time < prev_time:
            return False
        time += task.get_duration()
        prev_time = time
    return time <= 1440

if __name__ == '__main__':
    for input_path in os.listdir('inputs/'):
        output_path = 'outputs/' + input_path[:-3] + '.out'
        tasks = read_input_file('inputs/' + input_path)
        output = solve(tasks)
        write_output_file(output_path, output)
        print(eval_igloos(tasks, output))

# 100 >> 5000/45000
# 150 >> 4300/25000
# 200 >> 3300/11500