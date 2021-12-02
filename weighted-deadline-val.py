# best combinations: 1.9, 0.8, 4 -> 3680337.903601282

from parse import read_input_file, write_output_file
import os
from igloovalue import eval_igloos

INCREASE_URGENCY = 1.0
DECREASE_URGENCY = 0
FAR_AWAY = 2


def get_value_per_time(task, time):
    return task.get_late_benefit(time + task.get_duration() - task.get_deadline()) / task.get_duration()

def heuristic_value(task, time):
    value_per_time = get_value_per_time(task, time)
    if time >= task.get_deadline():
        return value_per_time
    # if lots of time left do to task, decrease its urgency
    if task.get_deadline() - time > FAR_AWAY * task.get_duration():
        return DECREASE_URGENCY * value_per_time
    # otherwise, not much time left to do task, increase urgency
    return INCREASE_URGENCY * value_per_time

def get_output(tasks):
    time = 0
    tasks_to_do = []
    tasks_left = set(tasks)
    while time < 1440 and tasks_left:
        next_best = max(tasks_left, key=lambda task: heuristic_value(task, time))
        if next_best.get_duration() + time <= 1440:
            tasks_to_do.append(next_best.get_task_id())
            time += next_best.get_duration()
        tasks_left.remove(next_best)
    return tasks_to_do

def solve(tasks):
    """
    Args:
        tasks: list[Task], list of igloos to polish
    Returns:
        output: list of igloos in order of polishing  
    """ 
    # best_order = []
    # global INCREASE_URGENCY, DECREASE_URGENCY, FAR_AWAY
    # for INCREASE_URGENCY in [1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0]:
    #     for DECREASE_URGENCY in [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]:
    #         for FAR_AWAY in [2, 3, 4, 5, 6]:
    #             new_order = get_output(tasks)
    #             if eval_igloos(tasks, new_order)[0] > eval_igloos(tasks, best_order)[0]:
    #                 best_order = new_order
    #                 print(INCREASE_URGENCY, DECREASE_URGENCY, FAR_AWAY)
    # return best_order
    return get_output(tasks)

total = 0
if __name__ == '__main__':
    # for input_size in ['small/', 'medium/', 'large/']:
    #     for input_path in os.listdir('inputs/' + input_size):
    #         output_path = 'outputs/' + input_size + input_path[:-3] + '.out'
    #         if input_path[0] != '.':
    #             tasks = read_input_file('inputs/' + input_size + input_path)
    #             output = solve(tasks)
    #             write_output_file(output_path, output)
    #             total += eval_igloos(tasks, output)[0]
    #         # print(input_path)
    tasks = read_input_file('inputs/small/small-74.in')
    output = solve(tasks)
    write_output_file("outputs/small/small-74.in", output)
    print(eval_igloos(tasks, output))