#!/bin/python
import sys

def hourglass_sum(mat):


    def hourgl(i, j, mat):
        elems = [mat[i][j], mat[i][j+1], mat[i][j+2], mat[i+1][j+1], mat[i+2][j], mat[i+2][j+1], mat[i+2][j+2]]
        return sum(elems)

    largest_sum = hourgl(0, 0, mat)

    for i in xrange(4):
        for j in xrange(4):
            if largest_sum < hourgl(i, j, mat):
                largest_sum = hourgl(i, j, mat)

    return largest_sum

# arr = []
# for arr_i in xrange(6):
#     arr_temp = map(int,raw_input().strip().split(' '))
#     arr.append(arr_temp)
# arr = [[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [0, 9, 2, -4, -4, 0], [0, 0, 0, -2, 0, 0], [0, 0, -1, -2, -4, 0]]
arr = [[-1, -1, 0, -9, -2, -2], [-2, -1, -6, -8, -2, -5],\
    [-1, -1, -1, -2, -3, -4], [-1, -9, -2, -4, -4, -5],\
    [-7, -3, -3, -2, -9, -9], [-1, -3, -1, -2, -4, -5]]

print hourglass_sum(arr)
