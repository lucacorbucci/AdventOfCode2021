import sys
sys.path.append("..")
from lib.utils import Utils

def solution(measurements):
	count = 0
	for index in range(1, len(measurements)): 
		if measurements[index] > measurements[index-1]:
			count += 1

	return count

measurements = Utils().read_lines_int("./input.txt")
print(solution(measurements))