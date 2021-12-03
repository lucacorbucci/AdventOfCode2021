import sys
sys.path.append("..")
from lib.utils import Utils

def solution(measurements):
	index, count = 0, 0
	previous_sum = sum(measurements[index:index+3])

	for index in range(1, len(measurements)-1):
		current_sum = sum(measurements[index:index+3])
		if current_sum > previous_sum:
			count += 1
		previous_sum = current_sum

	return count

measurements = Utils().read_lines_int("./input.txt")
print(solution(measurements))