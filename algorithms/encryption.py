import sys
import math

s = raw_input().strip().replace(' ', '')
length = len(s)
square = math.sqrt( length )

rows = int( math.floor( square ) )
cols = int ( math.ceil( square ) )

# print 'rows, cols, ', rows, cols

word_index = 0
matr =  [['' for x in range(cols)] for y in range(rows)]
for i in range(rows):
    for j in range(cols):
        if word_index <= length:
            matr[i][j] = s[word_index]
        else:
            matr[i][j] = ''
        word_index += 1



# print matr
out = []
for i in range(cols):
    for j in range(rows):
        out.append( matr[j][i] )
    out.append(' ')

print ''.join(out)
