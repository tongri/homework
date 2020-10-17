fizz = int(input("Enter the first number:"))
buzz = int(input("Enter the second one:"))
gazz = int(input("Enter the third one:"))
r = gazz + 1

for x in range(1, r):
	if not x % fizz and not x % buzz:
		print("FB")

	elif not x % fizz:
		print("F")

	elif not x % buzz:
		print("B")

	else:
		print(x)

print("The end.")