def is_isogram(st):
    s = st.lower()
    return len(set(s)) == len(s)

print is_isogram("moOse")
