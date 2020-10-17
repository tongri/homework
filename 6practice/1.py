appropriate = {}

while True:
	name = input("Введите имя ученика: ")
	marks = input("Введите оценки через запятую с пробелом: ")
	marks = list(map(lambda x: int(x), marks.split(", ")))
	checker = input("Введите да, если хотите продолжить: ")
	appropriate.update({name: marks})

	if checker != "да":
		break


new = {}


for x, y in appropriate.items():
	res = sum(y)/len(y)
	new.update({x: res})


highest = max(new.values())
lowest = min(new.values())

#print(str(highest) + " " + new[highest])
more = tuple(sorted(new.items(), key = lambda x: x[1]))
#print(sorted(new.items(), key = lambda x: x[1]))
print(str(more[0][1]) + " средняя оценка " + more[0][0] + " - он учится хуже всех")
print(str(more[-1][1]) + " средняя оценка " + more[-1][0] + "он учится лучше")
