def realize (uno, dos):
	difference = map(lambda x, y: len(x)-len(y) if len(x)>len(y) else len(y) - len(x), uno, dos)
	print("The biggest difference in length is " + str(max(difference)))

try:
	with open("unos.txt", "r") as f:
		uno = [l.strip() for l in f]
		#print(uno)


	with open("dost.txt", "r") as f:
		dos = [l.strip() for l in f]
		#print(dos)

except:
	print("Oh no !!! wrong path to file")

else:
	realize(uno, dos)

finally:
	print("Here we are")


#realize(uno, dos)