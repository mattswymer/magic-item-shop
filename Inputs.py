# Choose an option
print("1: village")
print("2: town")
print("3: city")
settlement_size = int(input("Enter a number: "))

if settlement_size == 1:
	settlement_size = "village"
elif settlement_size == 2:
	settlement_size = "town"
elif settlement_size == 3:
	settlement_size = "city"
else:
	print("Invalid input!")
