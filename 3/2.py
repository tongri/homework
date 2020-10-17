import re

with open("2.txt", "r") as f:
	for line in f:
		print ("\n")
		pattern = re.compile("[0-9]+")
		result = pattern.findall(line)
		for x in range(1, int(result[2]) + 1):
			if not x % int(result[0]) and not x % int(result[2]):
				print("FB ", end = "")

			elif not x % int(result[0]):
				print("F ", end = "")

			elif not x % int(result[1]):
				print("B ", end = "")

			else:
				print(str(x) + " ", end = "")