from time import sleep
def gen(n):
    for _ in range(n):
        yield _
        # sleep(0.5)



for a in gen(20):
    print a
