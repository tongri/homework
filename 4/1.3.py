nums = ["1", "3", "10", "45", "12"]

def increase(x, nums):
	nums = [int(num)+x for num in nums]
	new = map(str, nums)
	print(" ".join(new))

print(" ".join(nums))

x = int(input("How much would u like 2 add to each of them? "))

increase(x, nums)

