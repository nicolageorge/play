import itertools

def middle_permutation(strng):
    ret = []
    for i in itertools.permutations(strng):
        ret.append(''.join(i))
    ret = sorted(ret, key=str.lower)
    print ret
    middle = float(len(ret))/2
    if middle % 2 != 0:
        return ret[int(middle - .5)]
    else:
        return ret[int(middle)-1]

# Test.assert_equals(middle_permutation("abcdxgz"),"dczxgba")
print middle_permutation("cabd")
