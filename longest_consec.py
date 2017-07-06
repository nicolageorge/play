# def testing(actual, expected):
#     Test.assert_equals(actual, expected)
#
# Test.describe("longest_consec")
# Test.it("Basic tests")
# testing(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2), "abigailtheta")
# testing(longest_consec(["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"], 1), "oocccffuucccjjjkkkjyyyeehh")
# testing(longest_consec([], 3), "")
# testing(longest_consec(["itvayloxrp","wkppqsztdkmvcuwvereiupccauycnjutlv","vweqilsfytihvrzlaodfixoyxvyuyvgpck"], 2), "wkppqsztdkmvcuwvereiupccauycnjutlvvweqilsfytihvrzlaodfixoyxvyuyvgpck")
# testing(longest_consec(["wlwsasphmxx","owiaxujylentrklctozmymu","wpgozvxxiu"], 2), "wlwsasphmxxowiaxujylentrklctozmymu")
# testing(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], -2), "")
# testing(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 3), "ixoyx3452zzzzzzzzzzzz")
# testing(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 15), "")
# testing(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 0), "")
import collections
def longest_consec(strarr, k):
    ret = ""
    d = collections.defaultdict(int)
    n = len(strarr)
    if n == 0 or k > n or k <= 0:
        return ""
    for i, w in enumerate(strarr):
        d[i] = len(w)
    s = sorted(d, key=d.get, reverse=True)
    for i in range(0, k):
        # print i
        # print strarr[s[i]]
        ret += strarr[s[i]]
    return ret


print longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 3) #, "ixoyx3452zzzzzzzzzzzz")
