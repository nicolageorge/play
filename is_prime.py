def is_prime(num):
    if num in [-1, 0, 1]:
        return False
    for i in range(2, num+1):
        if num % i == 0:
            return False
    return True

print is_prime(4)
