#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Yee_172'
__date__ = '2017/12/09'


import numpy as np


M_MATRIX = np.array([[0.30, 0.42, 0.17, 0.11],
                     [0.33, 0.06, 0.27, 0.34],
                     [0.72, 0.07, 0.12, 0.09],
                     [0.42, 0.24, 0.28, 0.06]])
X = np.array([0, 1, 0, 0])
# X = np.array([0, 0.2, 0.7, 0.1])
# Next step


print(''.center(40, '-'))
print('Markov Matrix:')
print(M_MATRIX)
print('\nInitial Probability of events:')
print('Event_1: %g' % X[0])
print('Event_2: %g' % X[1])
print('Event_3: %g' % X[2])
print('Event_4: %g' % X[3])
print(''.center(40, '-'))


# Could use Fast Exponentiation to accelerate
M_1 = M_MATRIX
M_2 = M_25 = np.eye(4)
for _ in range(2):
    M_2 = np.dot(M_2, M_MATRIX)
M_3 = np.dot(M_2, M_MATRIX)
for _ in range(25):
    M_25 = np.dot(M_25, M_MATRIX)
M_50 = np.dot(M_25, M_25)
M_100 = np.dot(M_50, M_50)


print()
print(''.center(40, '-'))
print('Markov Matrix ^ 1:')
print(M_1)
x = np.dot(X, M_1)
print('\nProbability of events:')
print('Event_1: %g' % x[0])
print('Event_2: %g' % x[1])
print('Event_3: %g' % x[2])
print('Event_4: %g' % x[3])
print(''.center(40, '-'))
print()
print(''.center(40, '-'))
print('Markov Matrix ^ 2:')
print(M_2)
x = np.dot(X, M_2)
print('\nProbability of events:')
print('Event_1: %g' % x[0])
print('Event_2: %g' % x[1])
print('Event_3: %g' % x[2])
print('Event_4: %g' % x[3])
print(''.center(40, '-'))
print()
print(''.center(40, '-'))
print('Markov Matrix ^ 3:')
print(M_3)
x = np.dot(X, M_3)
print('\nProbability of events:')
print('Event_1: %g' % x[0])
print('Event_2: %g' % x[1])
print('Event_3: %g' % x[2])
print('Event_4: %g' % x[3])
print(''.center(40, '-'))
print()
print(''.center(40, '-'))
print('Markov Matrix ^ 25:')
print(M_25)
x = np.dot(X, M_25)
print('\nProbability of events:')
print('Event_1: %g' % x[0])
print('Event_2: %g' % x[1])
print('Event_3: %g' % x[2])
print('Event_4: %g' % x[3])
print(''.center(40, '-'))
print()
print(''.center(40, '-'))
print('Markov Matrix ^ 50:')
print(M_50)
x = np.dot(X, M_50)
print('\nProbability of events:')
print('Event_1: %g' % x[0])
print('Event_2: %g' % x[1])
print('Event_3: %g' % x[2])
print('Event_4: %g' % x[3])
print(''.center(40, '-'))
print()
print(''.center(40, '-'))
print('Markov Matrix ^ 100:')
print(M_100)
x = np.dot(X, M_100)
print('\nProbability of events:')
print('Event_1: %g' % x[0])
print('Event_2: %g' % x[1])
print('Event_3: %g' % x[2])
print('Event_4: %g' % x[3])
print(''.center(40, '-'))
