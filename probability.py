
answers = 4
questions = 1

# Initializes all the variables
def init(q, a):
    global answers
    global questions
    questions = q
    answers = len(a)

# Returns the probability as a percentage given a number of events, taking into account the possibilities computed before
def computeProbability(events, possibilities):
	return (events / possibilities) * 100

# Returns how much is added or substracted given a number of correct answers taking into account the number of questions
# Assuming addition of one point for a right answers and substraction of 0.33 for a wrong answer
def score(correctAnswers):
	positive = 1
	negative = 1 / (answers - 1)
	return positive * correctAnswers - ((questions - correctAnswers) * negative)

# Returns the added probability for a given condition
# Possible conditions are: an positive number of points, a negative number or zero
def conditionalProbability(rightAnswers, condition, possibilities):
	p = 0
	for i in range(0, len(rightAnswers)):
		if condition(score(i)):
			p = p + computeProbability(rightAnswers[i], possibilities)
	return p

def isPositive(score):
	return score > 0

def isNegative(score):
	return score < 0

def isZero(score):
	return score == 0
