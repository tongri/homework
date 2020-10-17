with open("3.txt", "r") as f:
	for line in f:
		sike = line.strip().split(";")
		first = sike[0].split()
		result = sike[1].split()
		first = list(map(lambda x: int(x), first))
		aver = int(sum(first)/len(first))
		ost = sum(first)%len(first)
		if aver == int(result[0]) and ost == int(result[1]):
			print(line.strip() + " True")
		else:
			print(line.strip() + " False")