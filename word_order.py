# is2 Thi1s T4est 3a" the function should return "Thi1s is2 3a T4est

def order(sentence):
    if sentence in [0, "0"]:
        return ''
    words = sentence.split(" ")
    ret = range(len(words))
    for w in words:
        for l in w:
            if l.isdigit():
                ret[int(l)-1] = w
    return " ".join(str(w) for w in ret)

print order(0)
