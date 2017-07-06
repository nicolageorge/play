# class that creates callable adder instances
class Adder(object):
    def __init__(self, n):
        self.n = n
    def __call__(self, m):
        return self.n + m
add5 = Adder(5)
add10 = Adder(10)
# print add5(20)
# print add10(100)


# using closures
def make_adder(n):
    def adder(m):
        return m+n
    return adder
add5_f = make_adder(5)
# print add5_f(200)


#python binds variables in closures by name
adders = []
for n in range(5):
    adders.append(lambda m: m+n)
# print [adder(10) for adder in adders]
# will print [14, 14, 14, 14, 14]


adders = []
for n in range(5):
    adders.append(lambda m, n = n : m + n)
# print [adder(10) for adder in adders]
# will print [10, 11, 12, 13, 14]

add4 = adders[4]
print add4(10, 100)
