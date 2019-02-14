import brute_force  # Possibilities generation by listing all of them
import probability # Computes probabilities and conditional probability



def showAnalysis(rightAnswers, possibilities):
	print()
	print('Hay', len(answers)**questions, 'posibilidades en total')
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

# Ask for parameters
questions = int(input('Número de preguntas: '))
show = input('¿Mostrar posibilidades? (s/n) ')
# Initialize stuff
answers = list('abcd')
brute_force.init(questions, show, answers)
# Compute all possible answers
brute_force.computePossibilities(questions, '')
# Print data analysing possibilities, probabilities and scores
showAnalysis(brute_force.rightAnswers, brute_force.possibilities)
