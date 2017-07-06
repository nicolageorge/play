def is_valid_IP(strng):
    aux = strng.split(".")
    if len(aux) != 4:
        return False
    for a in aux:
        try:
            if int(a) not in range(255)\
                or len(a) != len(str(int(a))):
                return False
        except ValueError:
            return False
    return True

print is_valid_IP("123.0.0.0")
