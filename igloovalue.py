import Task

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