# take highest profit/duration first, but run over array to decay values after each step

from parse import read_input_file, write_output_file
import os
from igloovalue import eval_igloos
import random

def get_value(task, time):
    return task.get_late_benefit(time + task.get_duration() - task.get_deadline())

def get_value_per_time(task, time):
    return task.get_late_benefit(time + task.get_duration() - task.get_deadline())/task.get_duration()

def get_duration(task, time):
    return -task.get_duration()

def get_deadline(task, time):
    return task.get_deadline()

funcs = [get_value_per_time, get_deadline]


def solve(tasks):
    """
    Args:
        tasks: list[Task], list of igloos to polish
    Returns:
        output: list of igloos in order of polishing  
    """ 
    time = 0
    tasks_to_do = []
    curr_vals = {task: task.get_max_benefit() for task in tasks}
    while time < 1440 and curr_vals:
        func = random.choice(funcs)
        next_best = max(curr_vals, key=lambda task: func(task, time))
        if next_best.get_duration() + time <= 1440:
            tasks_to_do.append(next_best.get_task_id())
            time += next_best.get_duration()
        del curr_vals[next_best]
    return tasks_to_do

if __name__ == '__main__':
    for input_size in ['small/', 'medium/', 'large/']:
        for input_path in os.listdir('inputs/' + input_size):
            output_path = 'outputs/' + input_size + input_path[:-3] + '.out'
            if input_path[0] != '.':
                tasks = read_input_file('inputs/' + input_size + input_path)
                output = solve(tasks)
                write_output_file(output_path, output)
