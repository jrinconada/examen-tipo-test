import brute_force  # Possibilities generation by listing all of them
import probability # Computes probabilities and conditional probability
import combinatorics # Computes possibilities using combinatorics

def showAnalysis(rightAnswers, possibilities):
	print()
	print('Hay', possibilities, 'posibilidades en total')
	print()
	print('Hay', rightAnswers[0], 'posibilidades de fallar todas las preguntas, hay un', probability.computeProbability(rightAnswers[0], possibilities), '% de probabilidad de que pase, obteniendo', probability.score(0), 'puntos.')
	for i in range(1, len(rightAnswers) - 1):
		print('Hay', rightAnswers[i], 'posibilidades de acertar', i, 'preguntas, hay un', probability.computeProbability(rightAnswers[i], possibilities), '% de probabilidad de que pase, obteniendo', probability.score(i), 'puntos.')
	print('Hay', rightAnswers[-1], 'posibilidad de acertar todas las preguntas, hay un', probability.computeProbability(rightAnswers[-1], possibilities), '% de probabilidad de que pase, obteniendo', probability.score(questions), 'puntos.')
	print()
	print('La probabilidad de sumar puntos es', probability.conditionalProbability(rightAnswers, probability.isPositive, possibilities), '%')
	print('La probabilidad de restar puntos es', probability.conditionalProbability(rightAnswers, probability.isNegative, possibilities), '%')
	print('La probabilidad de quedarse igual es', probability.conditionalProbability(rightAnswers, probability.isZero, possibilities), '%')

# Main

# Number of choices and number of answers
answers = list('abcd')
questions = int(input('Número de preguntas: '))
probability.init(questions, answers)

# ¿Show all possibilities?
show = input('¿Mostrar posibilidades? (s/n) ')
if show == 's' and questions > 8:
	print('Son demasiadas posibilidades para mostrar')
	show = 'n'

if show == 's': # Brute force it to show every possibility
	# Initialize and compute all possible answers
	brute_force.init(questions, show, answers)
	brute_force.computePossibilities(questions, '')
	# Print data analysing possibilities, probabilities and scores
	showAnalysis(brute_force.rightAnswers, brute_force.possibilities)
else: # Calculate using formula
	combinatorics.init(questions, answers)
	combinatorics.computePossibilities()
	showAnalysis(combinatorics.rightAnswers, combinatorics.possibilities)
