money = int(input("Enter a sum of money: "))
av = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000]
number = 1
rest = 0
diff = 0


while money:
	money = str(money)
	rest = money[-number]
	money = int(money)
	rest = int(rest)
	if rest and not diff:
		for x in range(1, rest+1):
			print("Take " + str(av[diff]) + " grn.")
		money -= rest
		diff += 1
		for i in av[1:3]:	
			for c in range(1,11):
				if not money:
					break
				else:
					money -= i
					print("Take " + str(i) + " grn.")
	elif not rest and not diff:
		for x in range(1, 11):
			print ("Take 1 grn.")
			money -= 1
		diff += 1
		for i in av[1:3]:	
			for c in range(1,11):
				if not money:
					break
				else:
					money -= i
					print("Take " + str(i) + " grn.")
			if money >= av[-diff]:
				money -= av[-diff]
				print("Take " + str(av[-diff]))
			else:
				diff += 1
	else:
		while money:
			if money >= av[-diff]:
				money -= av[-diff]
				print("Take " + str(av[-diff]))

			else:
				diff += 1

print("Here we are.")