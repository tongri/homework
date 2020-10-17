import re
b = []


with open("2.txt", "r") as f:
	for line in f:
		print ("\n")
		pattern = re.compile("[0-9]+")
		result = pattern.findall(line)
		for x in range(1, int(result[2]) + 1):
			if not x % int(result[0]) and not x % int(result[2]):
				b.append("FB")

			elif not x % int(result[0]):
				b.append("F")

			elif not x % int(result[1]):
				b.append("B")

			else:
				b.append(str(x))

		print(" ".join(b))