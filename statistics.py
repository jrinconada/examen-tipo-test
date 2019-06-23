import numpy as np
import scipy.stats as ss

answers = 4
questions = 10
p = 1 / answers

distribution = ss.binom(questions, p)

for i in range(questions + 1):
    print('Hay un ', distribution.pmf(i) * 100, '% de probabilidad de acertar', i, 'preguntas.')
