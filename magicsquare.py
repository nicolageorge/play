#!/bin/python

import sys
def calculate_magic_square():
    n = 3
    matrix = [[0 for i in range(n)] for j in range(n)]
    nsqr = n**2
    i = 0
    j = n/2

    print "i", i
    print "j", j

    for k in range(1, nsqr+1):
        matrix[i][j] = k
        print i, j, k
        i -= 1
        j += 1
        if k%n == 0:
            i += 2
            j -= 1
        else:
            if j == n:
                j -= n
            else:
                if i < 0:
                    i += n
    print matrix

def calculate_magic_square_distance(mat):
    row_sum = []
    col_sum = [[], [], []]
    for i in xrange(3):
        # print s[i][0]
        row_sum.append(sum(s[i]))
        for j in xrange(3):
            col_sum[j].append(s[i][j])
    for i in xrange(3):
        col_sum[i] = sum(col_sum[i])
    all_sum = sum(row_sum) + sum(col_sum)
    return abs(90 - all_sum)/2

# s = []
# for s_i in xrange(3):
#     s_temp = map(int,raw_input().strip().split(' '))
#     s.append(s_temp)
#  Print the minimum cost of converting 's' into a magic square
# s = [[4, 9, 2], [3, 5, 7], [8, 1, 5]]
s = [[4, 8, 2], [4, 5, 7], [6, 1, 6]]
calculate_magic_square_distance(s)
