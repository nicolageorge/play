#!/bin/python

import sys

def richieRich(digit_no, n, k):
    mid = len(n)/2
    first_half = list(n[:mid])
    second_half = list(n[mid:])
    rev_sec_half = second_half[::-1]
    # print first_half, second_half, rev_sec_half

    diff_no = 0
    change_counter = 0
    for i in range(len(first_half)):
        if first_half[i] != rev_sec_half[i]:
            diff_no += 1

    if diff_no > k:
        return -1

    two_digit_changes = k - diff_no
    print two_digit_changes

    if two_digit_changes == 0:
        for i in range(len(first_half)):
            if first_half[i] > rev_sec_half[i]:
                rev_sec_half[i] = first_half[i]
            else:
                first_half[i] = rev_sec_half[i]
    else:
        for i in range(len(first_half)):
            if two_digit_changes > 1:
                first_half[i], rev_sec_half[i] = 9, 9
                two_digit_changes -= 2

    print diff_no, change_counter
    new_word = first_half + rev_sec_half[::-1]
    return ''.join(str(x) for x in new_word)



[digit_no, k] = map(int, raw_input().strip().split(' '))
n = raw_input().strip()
result = richieRich(digit_no, n, k)
print(result)
