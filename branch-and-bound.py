from parse import read_input_file, write_output_file
import os
from igloovalue import eval_igloos
from itertools import permutations
from functools import lru_cache
import importlib

baseline = importlib.import_module("greedy-with-decay")

def solve(tasks):
    """
    Args:
        tasks: list[Task], list of igloos to polish
    Returns:
        output: list of igloos in order of polishing  
    """
    return find_best_seq(tasks)

def find_best_seq(tasks):
    n = len(tasks)
    # 2^n with DP

    lower_bound = eval_igloos(tasks, baseline.solve(tasks))[0]

    @lru_cache
    def helper(time, bitmask):
        if time >= 1440 or '0' not in bin(bitmask):
            return 0, []
        best_val, best_seq = 0, []
        for i in range(len(tasks)):
            task = tasks[i]
            if not (bitmask >> i) & 1: # if ith task is not used
                curr_val = 0
                if task.get_duration() + time <= task.get_deadline():
                    curr_val = task.get_max_benefit()
                else:
                    curr_val = task.get_late_benefit(task.get_duration() + time - task.get_deadline())
                if upper_bound(tasks, time, curr_val, bitmask) <= 3636.4106:
                    return
                updated_bitmask = bitmask | (1 << i)
                next_val, next_seq = helper(time + task.get_duration(), updated_bitmask)
                if next_val + curr_val > best_val:
                    best_val, best_seq = next_val + curr_val, [task.get_task_id()] + next_seq
        return best_val, best_seq
    return helper(0, 0)[1]

def is_valid(tasks):
    prev_time = -1
    time = 0
    for task in tasks:
        if time < prev_time:
            return False
        time += task.get_duration()
        prev_time = time
    return time <= 1440

def upper_bound(tasks, time, curr_val, bitmask):
    total_val = 0
    tasks_not_done = []
    for i in range(len(tasks)):
        if not (bitmask >> i) & 1: # if ith task is not used
            tasks_not_done.append(task)
    tasks_not_done.sort(key=lambda task: -task.get_max_benefit() / task.get_duration())
    for task in tasks_not_done:
        if time >= 1440:
            return curr_val + total_val
        total_val += task.get_max_benefit()
        time += tsak.get_duration()

if __name__ == '__main__':
    # for input_size in ['small/', 'medium/', 'large/']:
    #     for input_path in os.listdir('inputs/' + input_size):
    #         output_path = 'outputs/' + input_size + input_path[:-3] + '.out'
    #         if input_path[0] != '.':
    #             tasks = read_input_file('inputs/' + input_size + input_path)
    #             output = solve(tasks)
    #             write_output_file(output_path, output)
    #             print(eval_igloos(tasks, output))
    tasks = read_input_file('inputs/small/small-1.in')
    output = solve(tasks)
    write_output_file("outputs/small/small1.out", output)
    print(eval_igloos(tasks, output))

# 100 >> 5000/45000
# 150 >> 4300/25000
# 200 >> 3300/11500