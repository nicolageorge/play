
def polygons(a, b, c, d):
    ret = [0, 0 ,0]
    s_lst = sorted([a, b, c, d])
    if s_lst[0] == s_lst[1] and s_lst[2] == s_lst[3] and s_lst[0] == s_lst[2]:
        ret[0] += 1
    elif s_lst[0] == s_lst[1] and s_lst[2] == s_lst[3]:
        ret[1] += 1
    else:
    	ret[2] += 1
    return ret
        
    
# Complete the function below.
arr = map(int, raw_input().strip().split(' '))
print arr



