russia = {
	"XXS": 42,
	"XS": 44,
	"S": 46,
	"M": 48,
	"L": 50,
	"XL": 52,
	"XXL": 54,
	"XXXL": 56,
}
def convertation(russia):
	required = input("Enter the size to convert: ").upper()
	claimed = russia[required]
	print("In russia it is " + str(claimed))
	print("In Germany it is " + str(claimed - 6))
	print("In the USA it is " + str(claimed -34))
	print("In France it is " + str(claimed - 4))
	print("In Great Britain it is " + str(claimed - 18))


convertation(russia)