'''
MUIA 2019/2020
Authors: Antonio Sejas, Danielle Pellegrino, Sergio Cavero
'''

# Multiplicative congruential generator


class IMSL:
    def __init__(self, x0=1, a=16807, m=2**31-1, b=0):
        self.xi = x0
        self.a = a
        self.m = m
        self.b = b
        self.i = 0

    def gen(self):
        self.i += 1
        temp = (self.a*self.xi+self.b)
        if temp > 2 ^ 32:
            print('we handle an overflow ok in %d with value %d' %
                  (self.i, temp))
        self.xi = temp % self.m
        return self.xi

    def gen_interval_0_1(self):
        return self.gen()/self.m
