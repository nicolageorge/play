import sys

def solve(grades):
    def nearest5(x, base=5):
        return int(base * round(float(x)/base))
    for g in grades:
        if g < 38:
            print g
        else:
            near5 = nearest5(g)
            if g - near5 > 0:
                print g
            else:
                print near5



n = int(raw_input().strip())
grades = []
for g in xrange(n):
    grades.append( int(raw_input().strip()) )
solve(grades)
