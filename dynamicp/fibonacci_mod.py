def mod_fib(t0, t1, n):
    fib = [0 for x in range(n+1)]
    fib[0] = t0
    fib[1] = t1
    i = 2
    while i <= n:
        fib[i] = fib[i-2] + fib[i-1]**2
        i += 1
    print i
    return fib[n]

[t0, t1, n] = map(int, raw_input().strip().split(' '))
print mod_fib(n)
