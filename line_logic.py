#!/usr/bin/env python3

from functools import reduce
from itertools import chain, zip_longest, product
from itertools import combinations_with_replacement

def flatten(listOfLists):
    "Flatten one level of nesting"
    return chain.from_iterable(listOfLists)


def table_transpose(table_list):
    return (list(ln) for ln in zip(*table_list))


def decided_dot_in_line(lines):
    def decided_dot(dots):
        if all(dots): return 1
        if not any(dots): return 0
        return -1

    return [[ decided_dot(dot) for dot in table_transpose(line) ]
            for line in lines ]

def generate_line(size, nums):
    def mk_blank_rl(blank_rl, idx_list):
        for i in idx_list:
            blank_rl[i] += 1
        return blank_rl

    def render(blank_rls, dot_rls):
        res = [ [0]* i[0] + [1] *i[1]
                for i in zip_longest(blank_rls, dot_rls, fillvalue=0) ]
        return flatten(res)

    if len(nums) == 0:
        return [[0] * size]
    req_size = sum(nums) + (len(nums) -1)
    float_spc = size - req_size
    box_idxs = range(len(nums) +1)

    blank_rl_base = [0] + [1] * (len(nums)-1) + [0]
    blank_rls = (mk_blank_rl(blank_rl_base.copy(), list(idx))
                 for idx in combinations_with_replacement(box_idxs, float_spc) )

    return [ list(render(brl, nums)) for brl in blank_rls ]

def count_rl(s, dot):
    out, count = s
    if dot == 1:
        count += 1
    if dot == 0:
        if count > 0:
            out = out + [count]
        count = 0
    return (out, count)

def mk_rl(_c):
    c = _c + [0] # add centinel
    out, _ = reduce(count_rl, c, ([], 0))
    return out

def naive_filter_screen(screen, cs):
    scr_cols = table_transpose(screen)
    return all([mk_rl(col) == g_col
                for col, g_col in zip(scr_cols, cs)])

def print_screens(screens):
    for scr in map(list, screens):
        print( '\n'.join([''.join(map(str,ln)) for ln in scr]))

def d_check(line, decided_line):
    return all([(l == d) if (d != -1) else True
                for l, d in zip(line, decided_line)])

def main():
    if len(ls) != lsize: print('error num ls')
    if len(cs) != csize: print('error num cs')

    lines = [generate_line(lsize, n) for n in ls]
    cols = [generate_line(csize, n) for n in cs]

    for i in range(10):
        col_var = list(map(len, cols))
        line_var = list(map(len, lines))
        print(col_var)
        print(line_var)

        print(reduce((lambda x,y: x*y), map(len, lines), 1))

        lines_d = decided_dot_in_line(lines)
        # print(lines_d)
        tr_lines_d = table_transpose(lines_d)
        cols = [[ cc for cc in cc_list if d_check(cc, ddl) ]
                  for cc_list, ddl in zip(cols, tr_lines_d)]

        cols_d =  decided_dot_in_line(cols)
        tr_cols_f = table_transpose(cols_d)

        lines = [[ lc for lc in lc_list if d_check(lc, ddl) ]
                 for lc_list, ddl in zip(lines, tr_cols_f)]
        n_line_var = list(map(len, lines))
        if n_line_var == line_var:
            break

    print(list(map(len, cols)))
    print(list(map(len, lines)))
    print(reduce((lambda x,y: x*y), map(len, lines), 1))

    # broute force check
    screens = [ screen for screen in product(*lines)
                if naive_filter_screen(screen, cs) ]
    print_screens(screens)

if __name__ == '__main__':
    #m = 5
    #ls = [[], [1], [5], [1,1,1], [ 1, 2 ], [2, 1]]

    # OK
    # m = 5
    # ls = [[1,1,1], [1,1], [1,1,1], [1,1], [1,1,1]]
    # cs = [[1,1,1], [1,1], [1,1,1], [1,1], [1,1,1]]

    # OK
    # lsize = 5
    # csize = 5
    # ls = [[2], [3], [4], [5], [1, 1]]
    # cs = [[3], [2], [4], [4], [1, 2]]

    # lsize = 10
    # csize = 10
    # ls = [[3], [1,1], [3], [2,1], [4,1], [10], [1], [1], [1,2,2], [1,3,2]]
    # cs = [[2,3], [4], [3,1], [2,2], [1,2], [1], [4,1], [1,1,1], [3,1,2], [2,2]]

    # naive NG
    lsize = 10
    csize = 10
    ls = [[2], [1,2,1], [1,4], [7], [6], [4], [3], [3], [1,2], [1,1]]
    cs = [[], [3], [2], [2,2], [10], [6], [7], [5,2], [], []]

    # lsize =15
    # ls = [[2,4,2], [1,9,1], [9], [4,3], [3,2,2,1],
    #       [3,2,4], [3,3,3], [3,5], [9], [11],
    #       [1,1,1,1], [1,1,4,2], [14], [2,5,3], [6],
    #       [4], [1,1], [1,1], [2,1,1,2], [5,5]]
    # csize = 20
    # cs = [[2,4], [1,1,1], [1,4,1,2], [9,2,1], [12,1,2],
    #       [4,3,4,2], [3,1,1,2,5,1], [3,3,2,5,3], [3,2,9], [3,3,4,3],
    #       [9,2,1], [7,2,2], [3,4,2], [1,2,1,3,1], [2]]

    main()
