# http://www.geeksforgeeks.org/number-n-digits-non-decreasing-integers/
# Number of n-digits non-decreasing integers
#
# Given an integer n > 0, which denotes the number of digits, the task to find
# total number of n-digit positive integers which are non-decreasing in nature.
# A non-decreasing integer is a one in which all the digits from left to right
# are in non-decreasing form. ex: 1234, 1135, ..etc.
# Note :Leading zeros also count in non-decreasing integers such as 0000, 0001, 0023, etc are also non-decreasing integers of 4-digits.
#
# Examples:
#
# Input : n = 1
# Output : 10
# Numbers are 0, 1, 2, ...9.
#
# Input : n = 2
# Output : 55
#
# Input : n = 4
# Output : 715
def number_digits(n):
    # a[i][j] - all possible numbers with i digits and j-starting digit
    a = [[0 for i in range(n)] for j in range(10)]
    print a

number_digits(10)
