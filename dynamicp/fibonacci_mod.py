def mod_fib(t1, t2, n):
    fib = [0 for x in range(n+1)]
    fib[1] = t1
    fib[2] = t2
    i = 3
    while i <= n:
        fib[i] = fib[i-2] + fib[i-1]**2
        i += 1
    # print i
    return fib[-1]

[t1, t2, n] = map(int, raw_input().strip().split(' '))
print mod_fib(t1, t2, n)
