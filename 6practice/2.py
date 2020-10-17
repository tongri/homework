
pyt = {"Anton", "Joe", "Jason"}
front = {"Sophie", "Michael", "Trevor"}
fulls = {"Anton", "Sophie", "John"}
java = {"Joe", "Franklin", "Michael"}

spisok = [pyt, front, fulls, java]

new = [x for i in spisok for x in i]
dic = dict(map(lambda x: (x, new.count(x)) , new))
fin = list(filter(lambda x: dic[x] >= 2, dic))

for x in fin:
	print("{} studies simalteniously in several groups\n".format(x))

not_fr = (pyt | fulls | java) - front

for x in not_fr:
	print("{} doesnt study front-end\n".format(x))

both = pyt | java


for x in both:
	print("{} studies Python or Java\n".format(x))