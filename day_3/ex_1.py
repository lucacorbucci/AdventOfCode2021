import sys
sys.path.append("..")
from lib.utils import Utils
import numpy as np
from collections import Counter

def split_bits(diagnostic_report):
	results = []
	for item in diagnostic_report:
		results.append([bit for bit in item])

	return results

def solution(diagnostic_report):
	gamma = int("".join([Counter(item).most_common()[0][0] for item in diagnostic_report]), 2)
	epsilon = int("".join([Counter(item).most_common()[-1][0] for item in diagnostic_report]), 2)
	return gamma*epsilon

diagnostic_report = split_bits(Utils().read_lines_str("./input.txt"))
diagnostic_report = np.array(diagnostic_report).T
print(solution(diagnostic_report))