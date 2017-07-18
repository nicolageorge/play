In case someone is interested, here was my approach(longest test case completed in 1.66sec out of 4seconds for pypy3).

I start with this algorithm:
http://stackoverflow.com/questions/6877249/find-the-number-of-occurrences-of-a-subsequence-in-a-string

However, instead of having an inner loop where you iterate over each char in the sequence, i unrolled it and tracked the current row(4 units long) for every possible inner letter pair(aa, bb, cc, ect.). So, I'd calculate all possible a??a on the first pass, all b??b on the second pass, ect.. Then, I summed the answers for every pass for my answer.


I agree that this is not a medium problem. After much messing around, I finally managed to get in running on Python with no timeouts.
Even with an O(n) time and O(1) space algorithm, Python can be limiting just based on lookup times and aritmetic operation time.
If you are close but can't quite make it without timeouts, try PyPy (I was able to use the code I wrote for Python 3 without alteration).
Also, in a similar vein list calls seem to be much more efficient than dictionary calls in PyPy (unlike Python where I found them to be similar) which is important for an algorithm where elements are accessed so often.
