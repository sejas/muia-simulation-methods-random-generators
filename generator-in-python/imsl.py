'''
MUIA 2019/2020
Authors: Antonio Sejas, Danielle Pellegrino, Sergio Cavero
'''

# multiplicative congruential generator with IMSL parameters


class IMSL_BASIC:
    def __init__(self, x0=1, a=16807, m=2**31-1, b=0):
        self.xi = x0
        self.a = a
        self.m = m
        self.b = b

    def gen(self):
        self.xi = (self.a*self.xi+self.b) % self.m
        return self.xi

    def gen_interval_0_1(self):
        return self.gen()/self.m


class IMSL_BASIC:
    def __init__(self, x0=1, a=16807, m=2**31-1, b=0):
        self.xi = x0
        self.a = a
        self.m = m
        self.b = b

    def gen(self):
        self.xi = (self.a*self.xi+self.b) % self.m
        return self.xi

    def gen_interval_0_1(self):
        return self.gen()/self.m
