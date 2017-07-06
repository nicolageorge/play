def fibonacci(n):
    history = {0:1, 1:1}

    def rec_fib(n, history):
        if n not in history:
            history[n] = rec_fib(n-1, history) + rec_fib(n-2, history)
        return history[n]

    numb = rec_fib(n, history)
    sum = 0
    for num in history.items():
        sum += num[1]
    return history[n-1]


print fibonacci(50) # 12586269025
