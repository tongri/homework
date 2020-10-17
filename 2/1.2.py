number = int(input("Enter a number:"))

if number % 2 and (not number % 15) and number % 10:
	print("you are right")
else:
	print("NO")