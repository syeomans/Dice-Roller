import random

def roll(inStr):
	"""
	Rolls a die roll formula. Returns the total and a list of dice rolls as a tuple.

	To roll with advantage, include an '*'. To roll with disadvantage, include an '_'.
	Example inputs: '8d6', '1d20*+3', '1d20_-1', '1d20+1d4+2', '1d20-1d6+1'
	"""
	# Split input string into a list of die roll formulas
	# 	example inStr: '1d20*+1d4-3'
	# 	example inList: ['1d20*', '1d4', '-3']
	inStr = inStr.replace('-', '+-') # Account for negative bonuses and rolls
	inList = inStr.split("+") # Split into list of [x]d[y] formulas

	# Initialize return variables
	resultList = []

	# Main loop: iterate through each individual [x]d[y] formula
	for formula in inList:

		# If this is a die roll formula (not a bonus), roll the dice
		if 'd' in formula:

			# Split string into number of dice to roll and number of sides on the die
			numDice, numSides = formula.split('d')
			# Number of dice should never be negative
			numDice = abs(int(numDice)) 
			# If rolling with advantage or disadvantage, remove the exra characters from the split string
			numSides = int(numSides[:-1]) if ('*' in formula or '_' in formula) else int(numSides)

			# If this is rolled with advantage, roll twice and take the highest
			if '*' in formula: 
				# Roll [numDice] number of [numSides] sided dice and save to :result:
				for i in range(0, numDice):
					result1 = random.randrange(1, numSides+1)
					result2 = random.randrange(1, numSides+1)
					result = max(result1, result2)

			# If this is rolled with disadvantage, roll twice and take the lowest
			elif '_' in formula: 
				# Roll [numDice] number of [numSides] sided dice and save to :result:
				for i in range(0, numDice):
					result1 = random.randrange(1, numSides+1)
					result2 = random.randrange(1, numSides+1)
					result = min(result1, result2)

			# Otherwise, roll once
			else:
				# Roll [numDice] number of [numSides] sided dice and save to :result:
				for i in range(0, numDice):
					result = random.randrange(1, numSides+1)

			# Check if formula is negative. If so, result should be negative. 
			if '-' in formula:
				result = result * -1
			
			# Append final result to the list of results
			resultList.append(result)

		# If this formula is a bonus, append to list of results
		else:
			resultList.append(int(formula))

	total = sum(resultList)
	return(total, resultList)

def estimateAverage(formula):
	"""
	Uses the Monte Carlo method to estimate the average value of a die roll formula.

	Simulates a die roll formula and tracks the average over 50,000 trials.
	Dependencies: random library and roll() function from this library
	"""
	# Inits
	total = 0.0
	numTrials=50000

	# Main loop
	for i in range(0, numTrials):
		thisRoll = roll(formula)[0]
		total += thisRoll

	estAvg = round(total/numTrials, 1)
	return(estAvg)

def estimateSuccess(formula, valueToBeat):
	"""
	Uses the Monte Carlo method to estimate the ods of success for a die roll formula and DC.

	Simulates a die roll formula and tracks the number of successes over 50,000 trials.
	Dependencies: random library and roll() function from this library
	"""
	# Inits
	hits = 0.0
	numTrials=50000

	# Main loop
	for i in range(0, numTrials):
		thisRoll = roll(formula)[0]
		if thisRoll >= valueToBeat:
			hits += 1

	estOdds = round(hits/numTrials, 2)
	return(estOdds)

