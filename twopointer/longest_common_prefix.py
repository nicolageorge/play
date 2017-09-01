
def LCP(s):
    s = sorted(s)

    a = s[0]
    b = s[-1]

    rez = 0
    common = []
    for i in range(len(a)):
        if len(b)>i and a[i] == b[i]:
            rez += 1
            print a[i]
            common.append(a[i])

    return rez, common




strs = ['asdf','asdqwe','asd123','asdasd']
print LCP(strs)
