import random

def roll(inStr):
	# Split input string into a list of die roll formulas
		# example inStr: '1d20+1d4+3'
		# example inList: ['1d20', '1d4', '3']
	inStr = inStr.replace('-', '+-') # Account for negative bonuses and rolls
	inList = inStr.split("+") # Split into list of [x]d[y] formulas

	# Initialize return variables
	resultList = []

	# Main loop: iterate through each individual [x]d[y] formula
	for formula in inList:

		# If this formula is a die roll formula (not a bonus), roll die formula
		if 'd' in formula:
			numDice, numSides = map(int, formula.split('d'))

			# If this formula is negative, result should be negative
			if '-' in formula:
				# Roll [numDice] number of [numSides] sided dice and append to return list
				numDice = numDice * -1
				for i in range(0, numDice):
					result = random.randrange(1, numSides+1) * -1
					resultList.append(result)

			# If the formula is not negative, continue as normal
			else:
				# Roll [numDice] number of [numSides] sided dice and append to return list
				for i in range(0, numDice):
					result = random.randrange(1, numSides+1)
					resultList.append(result)

		# If this formula is a bonus, append to result
		else:
			resultList.append(int(formula))

	total = sum(resultList)
	return(total, resultList)
