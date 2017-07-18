My simple solution of the order log n, it passed all test cases. My logic was that there was a
pattern between the actual time and the time displayed on the stop watch. Am I missing something here? Many of the solutions
here seem to take complex approaches.

rem = 3
while t > rem:
    t = t-rem
    rem *= 2

print(rem-t+1)
