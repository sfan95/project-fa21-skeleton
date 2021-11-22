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
    profit = 0
    igloos = []
    while time < 1440 and len(tasks) > 0:
        best = max(tasks, key = lambda task: task.get_max_benefit())
        end = best.get_duration() + time 
        time = end
        if end <= 1440:
            newprofit = best.get_max_benefit()
            profit += newprofit
            tasks = list(filter(
                lambda x: (x.get_late_benefit(end + x.get_duration() - x.get_deadline()) >= 0.5 * newprofit or x.get_deadline() > end) and (x.get_task_id() != best.get_task_id()), tasks))
            igloos.append(best.get_task_id())
        else:
            break
    return igloos

def eval_igloos(tasks, task_ids):
    """Calculates value of a sequence of igloo indices.
    IGLOOS - a list of igloos (Tasks)
    INDICES - a list of indices of polished igloo
    """
    total_val = 0
    time = 0
    for ind in task_ids:
        next_igloo = tasks[ind - 1]
        time += next_igloo.get_duration()
        deadline = next_igloo.get_deadline()
        if time <= deadline:
            total_val += next_igloo.get_max_benefit()
        else:
            total_val += next_igloo.get_late_benefit(time - deadline)

    assert time <= 1440

    total_profit = sum([task.get_max_benefit() for task in tasks])
    total_time = sum([task.get_duration() for task in tasks])
    upper_bound = total_profit * total_time / 1440
    return total_val, upper_bound

if __name__ == '__main__':
    for input_path in os.listdir('inputs/'):
        output_path = 'outputs/' + input_path[:-3] + '.out'
        tasks = read_input_file('inputs/' + input_path)
        output = solve(tasks)
        write_output_file(output_path, output)
        print(eval_igloos(tasks, output))