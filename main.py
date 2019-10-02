'''
MUIA 2019/2020
Authors: Antonio Sejas, Danielle Pellegrino, Sergio Cavero
'''

from imsl import IMSL

imsl = IMSL()

K = 10000  # limit
for i in range(K):
    print(imsl.gen())
