# 0.104
# take highest profit/duration first, but run over array to decay values after each step

from parse import read_input_file, write_output_file
import os
from igloovalue import eval_igloos

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
        next_best = max(curr_vals, key=lambda task: curr_vals[task] / task.get_duration())
        if next_best.get_duration() + time <= 1440:
            tasks_to_do.append(next_best.get_task_id())
            time += next_best.get_duration()
        del curr_vals[next_best]
        for task in curr_vals.keys():
            if time + task.get_duration() > task.get_deadline():
                curr_vals[task] = task.get_late_benefit(time + task.get_duration() - task.get_deadline())
    return tasks_to_do

if __name__ == '__main__':
    for input_path in os.listdir('inputs/'):
        output_path = 'outputs/' + input_path[:-3] + '.out'
        tasks = read_input_file('inputs/' + input_path)
        output = solve(tasks)
        write_output_file(output_path, output)
        print(eval_igloos(tasks, output))