x = True
while x:
	number = input("Guess my age:")
	if not number:
		print("Ah no... Here we go again (You left it empty)")

	elif int(number) == 17:
		print("Congratulations! It is actually 17.")
		x = False

	elif int(number) < 17:
		print("Try a bit higher")

	elif int(number) > 17:
		print("I am not so ancient")