n = int(raw_input().strip())
sticks = map(int, raw_input().strip().split(' '))

st = sorted(sticks, reverse=True)


while len(st):
    print len(st)
    smallest = st.pop()
    st = [ x-smallest for x in st if x-smallest > 0 ]
    # print st
