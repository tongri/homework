with open ("2.txt", "r") as f:
	trios = list(map(lambda x: x.split(), f.readlines()))
	for x in trios:
		for i in range(1, int(x[2]) + 1):
			if not i % int(x[0]) and not i % int(x[2]):
				print("FB ", end = "")

			elif not i % int(x[0]):
				print("F ", end = "")

			elif not i % int(x[1]):
				print("B ", end = "")

			else:
				print(str(i) + " ", end = "")
		print("\n")