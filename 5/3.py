stuff = []
amount = []

while True:
	stuff.append(input("Enter any subject: "))
	amount.append(str(input("Enter its quantity: ")))
	x = input("would u like to add smth else? (y/n): ")
	if x == "n":
		break
	else:
		continue

for st, am in zip(stuff, amount):
	print("Take " + am + " " + st + "(s) .")