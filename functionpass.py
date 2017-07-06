def fnc1(p1, p2, p3):
    print "p1: {}, p2: {}, p3: {}".format(p1, p2, p3)


def fnc2(p):
    p1 = "fnc2_pe1"
    p2 = "fnc2_pe2"
    return fnc1(p1, p2, p)


print fnc2("asdf")
