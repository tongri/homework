
class CoffeeMachine:
	amount_of_water = 100
	amount_of_grain = 40

	__current_garbage = 0
	__max_garbage = 50

	def clear(self):
		self.__current_garbage = 0
		print("Having cleared the machine")


	def is_full(self, additional):
		return self.__current_garbage + additional > self.__max_garbage


	def not_enough_water(self, decreaser):
		return self.amount_of_water - decreaser <= 0 

	def not_enough_grain(self, decreaser):
		return self.amount_of_grain - decreaser <= 0

	def increase_garbage(self, increaser):
		self.__current_garbage += increaser

	def make_americano(self):
		a = []
		if self.is_full(30):
			print("clearing the garbage...")
			self.clear()


		if self.not_enough_water(10):
			a.append('water');

		if self.not_enough_grain(5):
			a.append("grain")

		if a:
			for x in a:

				print("Not enough {}".format(x))
			return

		print("Take your americano")
		self.amount_of_water -= 10
		self.amount_of_grain -= 5
		self.__current_garbage += 30


	def make_espresso(self):
		a = []
		if self.is_full(5):
			print("clearing the garbage...")
			self.clear()


		if self.not_enough_water(8):
			a.append('water');

		if self.not_enough_grain(7):
			a.append("grain")

		if a:
			for x in a:
				print("Not enough {}".format(x))
			return

		print("Take your espresso")
		self.amount_of_water -= 8
		self.amount_of_grain -= 7
		self.__current_garbage += 5




class CoffeeMachineMilked(CoffeeMachine):
	amount_of_milk = 60

	def not_enough_milk(self, decreaser):
		return self.amount_of_milk - decreaser <= 0 


	def make_latte(self):
		a = []

		if self.is_full(2):
			
			self.clear()


		if self.not_enough_water(4):
			a.append('water')

		if self.not_enough_grain(5):
			a.append('grain')

		if self.not_enough_milk(5):
			a.append('milk')

		if a:
			for x in a:
				print('Not enough {}'.format(x))
			return

		print("Take your latte")
		self.amount_of_water -= 4
		self.amount_of_grain -= 5
		self.amount_of_milk -= 5
		self.increase_garbage(2)



	def make_capuccino(self):
		a = []
		if self.is_full(30):
			self.clear()


		if self.not_enough_water(3):
			a.append('water')

		if self.not_enough_grain(8):
			a.append('grain')

		if self.not_enough_milk(4):
			a.append('milk')

		if a:
			for x in a:
				print('Not enough {}'.format(x))
			return

		print("Take your latte")
		self.amount_of_water -= 4
		self.amount_of_grain -= 8
		self.amount_of_milk -= 5
		self.increase_garbage(30)







class CoffeeMachineMilkedBolgrad(CoffeeMachineMilked):
	amount_of_alcochole = 20

	def not_enough_alcochole(self, decreaser):
		return self.amount_of_alcochole - decreaser < 0


	def make_irish_coffee(self):
		a = []

		if self.is_full(10):
			self.clear()

		if self.not_enough_water(3):
			a.append('water')

		if self.not_enough_grain(4):
			a.append('grain')

		if self.not_enough_milk(5):
			a.append('milk')

		if self.not_enough_alcochole(4):
			a.append('alcochole')
		if a:
			print("Not enough {}".format(x for x in a))
			return
		print("Take your Irish Coffe")

		self.amount_of_water -= 3
		self.amount_of_milk -= 5
		self.amount_of_grain -= 4
		self.amount_of_alcochole -= 4
		self.increase_garbage(30)

cup = CoffeeMachineMilkedBolgrad()

for _ in range(10):
	cup.make_irish_coffee()
