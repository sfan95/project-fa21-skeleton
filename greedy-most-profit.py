from parse import read_input_file, write_output_file
import os

def solve(tasks):
    """
    Args:
        tasks: list[Task], list of igloos to polish
    Returns:
        output: list of igloos in order of polishing  
    """
    time = 0
    profit = 0
    igloos = []
    while time < 1440:
        best = max(tasks, key = lambda task: task.get_max_benefit())
        end = best.get_duration() + time 
        if end <= 1440:
            newprofit = best.get_max_benefit()
            profit += newprofit
            tasks = list(filter(lambda x: x.get_late_benefit(end + x.get_duration() - x.get_deadline() >= 0.5 * profit or x.get_deadline() > end, tasks)))
            igloos.append(best.get_task_id())
        else:
            break
    return igloos

if __name__ == '__main__':
    for input_path in os.listdir('inputs/'):
        output_path = 'outputs/' + input_path[:-3] + '.out'
        tasks = read_input_file(input_path)
        output = solve(tasks)
        write_output_file(output_path, output)