import re

with open("2.txt", "r") as f:
	with open("3.txt", "w") as t:
		for line in f:
			print ("\n")
			pattern = re.compile("[0-9]+")
			result = pattern.findall(line)
			t.write("\n")
			for x in range(1, int(result[2]) + 1):
				if not x % int(result[0]) and not x % int(result[2]):
					t.write("FB ")

				elif not x % int(result[0]):
					t.write("F ")
				elif not x % int(result[1]):
					t.write("B ")
				else:
					t.write(str(x) + " ")