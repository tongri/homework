money = int(input("Enter a sum of money: "))

av = [1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
number = 0

while money:
  if money >= av[number]:
    money -= av[number]
    print("Take " + str(av[number]))
  else:
    number += 1