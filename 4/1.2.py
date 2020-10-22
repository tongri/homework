#Восьмая задача проэкта Эйлера
#Найти наибольшее произведение тринадцати последовательных цифр в числе файла 1.2.txt

with open("1.2.txt", "r") as f:
	lines = f.readlines()
	
lines = [elems.rstrip() for elems in lines]
s = ''.join(lines)
b = []
y = 14


for x in range(1, len(s)-12):
	sli = s[x:y]
	y += 1
	if not "0" in sli:
		b.append(sli)


c = []


for z in b:
	k = 1
	for n in z:
		k *= int(n)
	c.append(k)

print(max(c))
