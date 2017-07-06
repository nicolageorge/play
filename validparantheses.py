def validBraces(string):
    start = [0, 0, 0] # () [] {}
    for c in string:
        if c == '(': start[0] += 1
        if c == ')': start[0] -= 1
        if c == '[': start[1] += 1
        if c == ']': start[1] -= 1
        if c == '{': start[2] += 1
        if c == '}': start[2] -= 1

        if start[0]<0 or start[1]<0 or start[2]<0: return False
    return start == [0, 0, 0]

print validBraces("[]")
