import rubik
import solver

def main():
    start = rubik.I
    end = rubik.perm_apply(rubik.F, start)
    ans = solver.shortest_path(start, end)
    print 'ans:{}'.format(ans)
    
    # self.assertEqual(len(ans), 1)
    # self.assertEqual(ans, [rubik.F])


if __name__ == '__main__':
    main()