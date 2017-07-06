def cond1(param):
    if param%2 == 0:
        return True
    else:
        return False

def cond2(param):
    return True if param%2 == 0 else False

def mod1(param):
    return param+1000

col1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
col2 = [a for a in range(0, 10)]
# print col1
# print col2

col3 = [p if cond1(p) else mod1(p) for p in col2]
# print col3

col4 = {i:chr(65+i) for i in range(20)}
# print col4

col5 = {chr(75+i) for i in range(15)}
# print col5

col6 = {i:str(i) for i in range(10)}
# print col6

def factorialR(N):
    assert isinstance(N, int) and N>=1
    print N
    return 1 if N <= 1 else N * factorialR(N-1)
# print factorialR(10)


# do_it = lambda f, *args: f(*args)
# hello = lambda first, last: print("hello", first, last)
# hello = lambda first, last: print("Hello", first, last)
# bye = lambda first, last: print("bye", first, last)
# _ = list(map(do_it, [hello, bye], ['david', 'jane'], ['mertz', 'bemve']))
# print _



def identity_print(x):
    print(x)
    return x
echo_FP = lambda: identity_print(input("FP --"))=='quit' or echo_FP()
# echo_FP()


hello = lambda name: print "Hello", name
hello("david")
