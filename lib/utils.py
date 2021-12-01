class Utils:
	def read_lines_int(self, file_path):
		with open(file_path) as file:
			lines = file.readlines()
			lines = [int(line.rstrip()) for line in lines]
			return lines