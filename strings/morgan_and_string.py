def merge_words(first_word, second_word):
    i, j = 0, 0
    rez = []
    while i < len(first_word) and j < len(second_word):
        if first_word[i] <= second_word[j]:
            rez.append(first_word[i])
            i += 1
        else:
            rez.append(second_word[j])
            j += 1
    if i < len(first_word):
        rez.extend( first_word[i:] )
    if j < len(second_word):
        rez.extend( second_word[j:] )
    return ''.join([x for x in rez])

inputs = int(raw_input().strip())
for i in range(inputs):
    first_word = '{}z'.format(raw_input().strip())
    second_word = '{}z'.format(raw_input().strip())
    print merge_words(first_word, second_word)
