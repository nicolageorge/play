import collections
# "din" => "((("
#
# "recede" => "()()()"
#
# "Success" => ")())())"
#
# "(( @" => "))(("


def duplicate_encode(word):
    ret = ""
    arranged_word = sorted(word)
    d = collections.defaultdict(int)
    for c in word:
        d[c.lower()] += 1

    for c in word:
        if d[c.lower()] == 1:
            ret += "("
        else:
            ret += ")"

    return ret


print duplicate_encode("recede")
