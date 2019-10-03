'''
MUIA 2019/2020
Authors: Antonio Sejas, Danielle Pellegrino, Sergio Cavero
'''

from imsl import IMSL

FILENAME = 'random-numbers-sample.txt'
K = 10000  # limit

imsl = IMSL()
with open(FILENAME, 'w') as f:
    for i in range(K):
        f.write('%.16f\n' % imsl.gen_interval_0_1())
