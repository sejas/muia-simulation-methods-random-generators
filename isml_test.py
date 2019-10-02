'''
MUIA 2019/2020
Authors: Antonio Sejas, Danielle Pellegrino, Sergio Cavero
'''

# Validate 32 bits Architectures, Park y Miller (1988)
from imsl import IMSL

imsl = IMSL(x0=1)

EXPECTED_VALUE = 1043618065
K = 10000  # limit
for i in range(K):
    latest = imsl.gen()

if latest == EXPECTED_VALUE:
    print('Everything ok, There is no overflow')
    print('The 10000th number is %s 👌' % EXPECTED_VALUE)
else:
    raise 'ERROR !! There is overflow.'
