import math

our_entrance = 1
our_floor = 1




def check (num, floors, flats):
	if num <= floors*flats*entrances:
		our_entrance = 1
		while num > floors*flats:
			num -= floors*flats
			our_entrance += 1
		our_floor = math.ceil(num/flats)
		return print("Необходимо зайти в " + str(our_entrance) + " подъезд, на " + str(our_floor) + " этаж.")
	else:
		return print("Неправильный номер квартиры")


num = int(input("Какой номер квартиры? "))
floors = int(input("Введите количество этажей: "))
flats = int(input("Введите количество квартир на этаже: "))
entrances = int(input("Введите число подъездов: "))



check(num, floors, flats)