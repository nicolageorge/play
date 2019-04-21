# def print(m):
#   row, col = 0, 0
#   for row in range(len(m))
def print_top_row(m, start, finish):
    

def spiral(m):
    a, b, c, d = 0, 0, 0, 1
    while(a <= len(m[0] or b <= len(m) or c <= len(m[0]) or d <= len(m)):
        print_top_row(m, a)
        a += 1
        print_right_row(m, b)
        b += 1
        print_bottom_row(m, c)
        c += 1
        print_left_row(m, d)
        d += 1

if __name__ == '__main__':
    main()  