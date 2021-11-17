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
    tasks.sort(key=lambda task: task.get_deadline())
    tasks_to_do = []
    prev_end_time = -1
    for task in tasks:
        if task.get_deadline() - task.get_duration() >= prev_end_time:
            tasks_to_do.append(task.get_task_id())
            prev_end_time = task.get_deadline()
        else:
            continue
    return tasks_to_do

if __name__ == '__main__':
    for input_path in os.listdir('inputs/'):
        output_path = 'outputs/' + input_path[:-3] + '.out'
        tasks = read_input_file('inputs/' + input_path)
        output = solve(tasks)
        write_output_file(output_path, output)
        print(eval_igloos(tasks, output))