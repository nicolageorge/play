text = 'the fox is in the hat'

search_text = 'the'

arr = [text[i:i+len(search_text)] for i in range(len(text)-len(search_text)+1)]


for i in range(10000000):
    h = hash(i)
    if i % 1000000 == 0:
        print h
