def sort_array(source_array):
    aux = []
    ret = []
    for i in source_array:
        if i % 2 != 0:
            aux.append(i)
    aux = sorted(aux)
    odd_numbers = get_numbers(aux)
    for i in source_array:
        if i % 2 != 0:
            ret.append(next(odd_numbers))
        else:
            ret.append(i)

    return ret

def get_numbers(list):
    for i in list:
        yield i


# Test.assert_equals(sort_array([5, 3, 2, 8, 1, 4]), [1, 3, 2, 8, 5, 4])
# Test.assert_equals(sort_array([5, 3, 1, 8, 0]), [1, 3, 5, 8, 0])
# Test.assert_equals(sort_array([]),[])

print sort_array([5, 3, 2, 8, 1, 4])
