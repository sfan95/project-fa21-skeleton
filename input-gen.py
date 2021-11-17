from random import randint, uniform

n = int(input())
print(n)
for i in range(n):
	task_id = i + 1
	deadline = randint(1, 1440)
	duration = randint(1, 60)
	profit = round(uniform(0.001, 99.999), 3)
	print("{0} {1} {2} {3}".format(task_id, deadline, duration, profit))