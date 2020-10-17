#Без циклов и модулей

def tidy(some):
	some = some.replace(".", "")
	some = some.replace('"', "")
	some = some.replace("\n", "")
	some = some.replace(":", "")
	some = some.replace(",", "")
	some = some.split()
	return some


with open("1.3.txt", 'r') as f:
	f = f.readlines()
	s = " ".join(f)
	new = tidy(s)
	new = list(filter(None, new))
	dic = dict(map(lambda x: (x, new.count(x)) , new))
	print(sorted(dic.items(), key = lambda x: x[1], reverse = True))