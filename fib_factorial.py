# suma factorialelor primelor n numere din sirul lui fibonaci
def fac(n):
    if n == 0:
        return 1
    else:
        return n * fac(n-1)

def sum_fib(n):
    fib_numbers = [0, 1]
    for i in range(2, n):
        fib_numbers.append( fib_numbers[i - 2] + fib_numbers[i - 1] )

    fib_num = [fac(n) for n in fib_numbers]
    return sum(fib_num)


print sum_fib(6)
