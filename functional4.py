import math
class RightTriangle(object):
    """Class used solely as namespace for related functions"""
    @staticmethod
    def hypotenuse(a, b):
        return math.sqrt(a**2 + b**2)

    @staticmethod
    def sin(a, b):
        return a / RightTriangle.hypotenuse(a, b)

    @staticmethod
    def cos(a, b):
        return b / RightTriangle.hypotenuse(a, b)



def get_primes():
    candidate = 2
    found = []
    while True:
        if all(candidate % prime != 0 for prime in found):
            yield candidate
            found.append(candidate)
        candidate += 1

primes = get_primes()

print next(primes)

print next(primes)
print next(primes)
print next(primes)
print next(primes)
print next(primes)
print next(primes)
