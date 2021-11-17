# 0.079

from parse import read_input_file, write_output_file
import os
from igloovalue import eval_igloos

def jobScheduling(ids, startTime, endTime, profit):
    jobs = []
    n = len(startTime)
    for i in range(n):
        jobs.append((startTime[i], endTime[i], profit[i], ids[i]))
    jobs.sort(key=lambda j: j[0])
    totalTime = max(endTime)
    
    memo = {}
    seq = {}
    
    def f(i, t):
        # max profit sequence for jobs[i...] where first available start time is t, O(nT)
        if (i, t) not in memo:
            if i >= n or t > totalTime:
                memo[(i, t)] = 0
                seq[(i, t)] = []
            elif jobs[i][0] < t:
                memo[(i, t)], seq[(i, t)] = f(i + 1, t) 
            else:
                profit_skip, seq_skip = f(i + 1, t)
                profit_curr, seq_curr = f(i + 1, jobs[i][1])
                profit_curr += jobs[i][2]
                if profit_curr >= profit_skip:
                    memo[(i, t)] = profit_curr
                    seq[(i, t)] = [jobs[i][3]] + seq_curr
                else:
                    memo[(i, t)] = profit_skip
                    seq[(i, t)] = seq_skip
        return memo[(i, t)], seq[(i, t)]
    
    return f(0, 0)

def solve(tasks):
    """
    Args:
        tasks: list[Task], list of igloos to polish
    Returns:
        output: list of igloos in order of polishing  
    """
    ids = [task.get_task_id() for task in tasks]
    starts = [task.get_deadline() - task.get_duration() for task in tasks]
    ends = [task.get_deadline() for task in tasks]
    profits = [task.get_max_benefit() for task in tasks]
    return jobScheduling(ids, starts, ends, profits)[1]

if __name__ == '__main__':
    for input_path in os.listdir('inputs/'):
        output_path = 'outputs/' + input_path[:-3] + '.out'
        tasks = read_input_file('inputs/' + input_path)
        output = solve(tasks)
        write_output_file(output_path, output)
        print(eval_igloos(tasks, output))