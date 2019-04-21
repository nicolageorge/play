def reverse_list(the_list):
    start = 0
    end = len(the_list) - 1
    while start <= end:
        the_list[start], the_list[end] = the_list[end], the_list[start]
        start += 1
        end -= 1
    return the_list


if __name__ == '__main__':
    the_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    lst = reverse_list(the_list)
    print(', '.join([str(i) for i in lst]))


    word = 'thiswillbereversed'
    rev_word = reverse_list(list(word))
    print(''.join([str(i) for i in rev_word]))
