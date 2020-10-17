def drawing (stars, *sike):
	sike = list(sike)
	if stars % 2 and stars > 0:
		for x in range(1, stars+1, 2):
			sike.append(x)
		sike = sike + sike[len(sike)-2::-1]
		for i in sike:
			of_sp = int((stars - i)/2)
			print(" "*of_sp + "*"*i + " "*of_sp)
	else:
		print("Сори - Вы ввели неправильное число, программу не запущу)))9)")


stars = int(input("Введите число(нечетное и положительное): "))
if stars == 1:
	print("*")
else:
	drawing(stars)