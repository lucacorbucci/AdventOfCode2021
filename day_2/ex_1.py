import sys
sys.path.append("..")
from lib.utils import Utils

def split_movements(movements):
	new_mov = []
	for movement in movements:
		movement = movement.split(" ")
		new_mov.append((movement[0], int(movement[1])))
	return new_mov

def solution(movements):
	pos_h, pos_d = 0, 0
	for movement in movements:
		if movement[0] == "forward":
			pos_h += movement[1]
		elif movement[0] == "down":
			pos_d += movement[1]
		else: 
			pos_d -= movement[1]
	return pos_d*pos_h

movements = Utils().read_lines_str("./input.txt")
movements = split_movements(movements)
print(solution(movements))