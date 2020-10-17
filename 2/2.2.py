number = int(input("Write a number:"))


print("It is odd" if number % 2 else "It is even")

print("It can be divided by 3 and 5" if not number % 3 and not number % 5 else "It cant be divided by 3 and 5")
