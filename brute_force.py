
possibilities = 0
rightAnswers = [0]
showPossibilites = False
answers = list('abcd')

# Initializes all the variables
def init(questions, show, options):
    global showPossibilites
    global possibilities
    global rightAnswers
    global answers
    showPossibilites = True if show == 's' else False
    answers = options
    rightAnswers = [0] * (questions + 1)

# Counts the number of correct answers given an outcome of chosen letters
# Assuming choice 'a' is the correct answer for all questions
def count(letters):
	global rightAnswers
	right = len(list(filter(lambda letter: letter == 'a', letters)))
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
