def realize (uno, dos):
	difference = map(lambda x, y: len(x)-len(y) if len(x)>len(y) else len(y) - len(x), uno, dos)
	print(max(difference))

uno = ["sfsdffs", "yugfvbjhr", "dlkfnjnslkescv"]
dos = ["bvbv", "fgfgfse", "iushdjn"]


realize(uno, dos)