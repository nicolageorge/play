# core patterns
# protocol view of python
# built in inheritance protocol and how it works
# caveats on how oo works in python


# some behaviour that I want to implement, write __ function
# top level function or top level syntax -> corresponding __

# x + y  -> __add__
# init x -> __init__
# repr(x)-> __repr__
#  x()   -> __call__


class Polynomial:
    def __init__(self, *coeffs):
        self.coeffs = coeffs

    def __repr__(self):
        return 'Polynomial(*{!r})'.format(self.coeffs)

    def __add__(self, other):
        return Polynomial( *(x+y for x, y in zip(self.coeffs, other.coeffs)) )

    def __len__(self):
        return len(self.coeffs)

    def __call__(self):
        pass




p1 = Polynomial()
p2 = Polynomial()

p1.coeffs = 1, 2, 3 #  x**2 + 2x + 3
p2.coeffs = 3, 4, 3 # 3x**2 + 4x + 3
