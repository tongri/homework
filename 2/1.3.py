number = int(input("Lets find all of them:"))
r = number + 1

for x in range(1, r):
	if not number % x:
		print(x)