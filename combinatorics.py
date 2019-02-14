from math import factorial

possibilities = 0
rightAnswers = [0]
answers = 4
questions = 1

# Initializes all the variables
def init(q, a):
    global showPossibilites
    global rightAnswers
    global answers
    global questions
    questions = q
    answers = len(a)
    rightAnswers = [0] * (q + 1)

# COMBINATORICS
def permutations(n,k):
    return factorial(n) / factorial(n - k)

def combinations(n,k):
    return permutations(n,k) / factorial(k)

# If there is only one right answer, the rest of the combinations of answers for every question possibilities to get it all wrong
def calculateZeroRight():
    return (answers - 1)**questions

# For every question there is a possibility of geting it right
# and multiply for all remaing possibilities of geting the rest wrong
def calculateOneRight():
    return questions * (answers - 1)**(questions - 1)

# For every possible combination of arraging n elements
# multiply all remaing possibilities of getting the rest wrong
def calculateNRight(n):
    return combinations(questions, n) * (answers - 1)**(questions - n)

# Only one possibility to get it all right
def calculateAllRight():
    return 1

# Given a number of questions computes all possible combinations of answers
def computePossibilities():
    global possibilities
    global rightAnswers
    # All possibilities
    possibilities = answers**questions
    # All wrong
    rightAnswers[0] = calculateZeroRight()
    # One right
    rightAnswers[1] = calculateOneRight()
    # n right (questions - n wrong)
    for i in range(2, len(rightAnswers) - 1):
        rightAnswers[i] = calculateNRight(i)
    # All right
    rightAnswers[-1] = calculateAllRight()
