Hi,

I solved this in linear time, without sorting. https://www.hackerrank.com/challenges/almost-sorted/submissions/code/11582796

What i did was:

(1)input the array in vector

(2)run through the vector from index 1 to len-2 ( leaving the first and last elements)

(3)At each of these indices check whether it forms an inversion or a reverse inversion. Inversion is if curr > prev && curr > next. Similarly find out reverse inversions, curr < prev && curr < next. I call inversions as dips, and reverse inversions as ups.

(4)for the first and last elements you can check only the next and prev respectively as they are at the boundary.

(5)Once you have collected data of these inversions, if you analyze you will see that if reverse has to form a soln, you will have only one dip and one up.

(6)And if swapping can be soln then there will be 2 dips and 2 ups.

(7)If you get more than 2 dips and 2ups, it means it can't be solved.

(8)There are some edge cases which you need to take care of though.
