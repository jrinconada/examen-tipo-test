
# Returns the probability as a percentage given a number of events, taking into account the possibilities computed before
def probability(events):
	return (events / possibilities) * 100

# Returns how much is added or substracted given a number of correct answers taking into account the number of questions
# Assuming addition of one point for a right answers and substraction of 0.33 for a wrong answer
def score(correctAnswers):
	positive = 1
	negative = 1 / (len(answers) - 1)
	return positive * correctAnswers - ((questions - correctAnswers) * negative)
	
# Returns the added probability for a given condition
# Possible conditions are: an positive number of points, a negative number or zero
def conditionalProbability(condition):
	p = 0
	for i in range(0, len(rightAnswers)):
		if condition(score(i)):
			p = p + probability(rightAnswers[i])
	return p
	
def isPositive(score):
	return score > 0

def isNegative(score):
	return score < 0

def isZero(score):
	return score == 0
	
# Counts the number of correct answers given an outcome of chosen letters
# Assuming choice 'a' is the correct answer for all questions
def count(letters):
	global rightAnswers
	right = 0
	for i in list(letters):
		if i == 'a':
			right = right + 1
	rightAnswers[right] = rightAnswers[right] + 1

# Given a contatenation of letters, adds one last letter for every possible choice,
# calls count function to look for correct answers and adds one to the number possibilities counted
# If show parameter is true prints the final contatenation and the number of possibilities computed until this point
def finalComputation(letters, show=True):
	global possibilities
	for i in answers:
		if show: print(letters + i, end=' | ')		
		count(letters + i)
		possibilities = possibilities + 1
	if show: print(possibilities, 'posibilidades')

# Given a number of questions computes all possible combinations of answers
# This is a recursive function, it will call itself with a new letter being concatenated until there is only one question left
def computePossibilities(questions, letters):
	if questions > 1:
		questions = questions - 1
		for i in answers:
			computePossibilities(questions, letters + i)
	else:
		finalComputation(letters, showPossibilites)

# Main

# Ask for parameters
questions = int(input('Número de preguntas: '))
show = input('¿Mostrar posibilidades? (s/n) ')
# Initialize stuff
showPossibilites = True if show == 's' else False
answers = list('abcd')
possibilities = 0
rightAnswers = [0] * (questions + 1)

# Compute all possible answers
computePossibilities(questions, '')

# Print data analysing possibilities, probabilities and scores
print()
print('Hay', len(answers)**questions, 'posibilidades en total')
print()
print('Hay', rightAnswers[0], 'posibilidades de fallar todas las preguntas, hay un', probability(rightAnswers[0]), '% de probabilidad de que pase, obteniendo', score(0), 'puntos.')
for i in range(1, len(rightAnswers) - 1):
	print('Hay', rightAnswers[i], 'posibilidades de acertar', i, 'preguntas, hay un', probability(rightAnswers[i]), '% de probabilidad de que pase, obteniendo', score(i), 'puntos.')
print('Hay', rightAnswers[-1], 'posibilidad de acertar todas las preguntas, hay un', probability(rightAnswers[-1]), '% de probabilidad de que pase, obteniendo', score(questions), 'puntos.')
print()
print('La probabilidad de sumar puntos es', conditionalProbability(isPositive), '%')
print('La probabilidad de restar puntos es', conditionalProbability(isNegative), '%')
print('La probabilidad de quedarse igual es', conditionalProbability(isZero), '%')
