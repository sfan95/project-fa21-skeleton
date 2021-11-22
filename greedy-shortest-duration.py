# 0.0747

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
    tasks = list(sorted(tasks, key=lambda task: task.get_duration()))
    tasks_to_do = []
    i = 0
    while time < 1440 and i < len(tasks):
        if tasks[i].get_duration() + time <= 1440:
            tasks_to_do.append(tasks[i].get_task_id())
            time += tasks[i].get_duration()
            i += 1
        else:
            i += 1
    return tasks_to_do

if __name__ == '__main__':
    for input_path in os.listdir('inputs/'):
        output_path = 'outputs/' + input_path[:-3] + '.out'
        tasks = read_input_file('inputs/' + input_path)
        output = solve(tasks)
        write_output_file(output_path, output)
        print(eval_igloos(tasks, output))