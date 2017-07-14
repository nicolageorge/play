import sys
sock_number = int(raw_input().strip())

sock_arr = map(int, raw_input().strip().split(' '))
pairs_counter = 0
checked_socks = []
for sock in sock_arr:
    if sock in checked_socks:
        pairs_counter += 1
        checked_socks.remove(sock)
    else:
        checked_socks.append(sock)

print pairs_counter
