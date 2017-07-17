n = int(raw_input().strip())

likes = 2
peeps = 2
for i in range(2, n+1):
    total_advertised = 3 * peeps
    peeps = total_advertised / 2
    likes += peeps
print likes
