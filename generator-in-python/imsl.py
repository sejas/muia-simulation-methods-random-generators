'''
MUIA 2019/2020
Authors: Antonio Sejas, Danielle Pellegrino, Sergio Cavero
'''

# multiplicative congruential generator with IMSL parameters


class IMSL_BASIC:
    def __init__(self, x0=1, a=16807, m=2**31-1, b=0):
        self.xi = x0
        self.xi_interval_0_1 = x0/m
        self.a = a
        self.m = m
        self.b = b

    def gen(self):
        self.xi = (self.a*self.xi+self.b) % self.m
        self.xi_interval_0_1 = self.xi / self.m
        return self.xi

    def gen_interval_0_1(self):
        self.gen()
        return self.xi_interval_0_1


class IMSL:
    """ Using Schrage method to avoid overflow """

    def __init__(self, x0=1, a=16807, m=2**31-1, b=0):
        self.xi = x0
        self.xi_interval_0_1 = x0/m
        self.a = a
        self.m = m
        self.b = b
        # Schrage extra variables
        self.q = m/a
        self.r = m % a

    def gen(self):
        hi = int(self.xi / self.q)
        lo = self.xi % self.q
        test = self.a * lo - self.r*hi
        if test > 0:
            self.xi = test
        else:
            self.xi = test + self.m
        self.xi_interval_0_1 = self.xi / self.m
        return self.xi

    def gen_interval_0_1(self):
        self.gen()
        return self.xi_interval_0_1
