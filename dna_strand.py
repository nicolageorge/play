def DNA_strand(dna):
    dict = { "A": "T", "T" : "A", "C" : "G", "G" : "C" }
    ret = ""
    for c in dna:
        ret += dict[c]
    return ret


def DNA_strand2(dna):
    dict = { "A": "T", "T" : "A", "C" : "G", "G" : "C" }
    return "".join( [dict[x] for x in dna] )
print DNA_strand2("ATTCCGGG")
