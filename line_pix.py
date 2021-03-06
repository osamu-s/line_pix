#!/usr/bin/env python3

### generate perm

import itertools

def generate_line(col, num):
    if num == 0:
        return [[0] * col]
    if num == col:
        return [[1] * col]
    if col == 0:
        return []   # not to be used

    return ([[0] + l for l in generate_line(col -1, num)] +
            [[1] + l for l in generate_line(col -1, num -1)] )


def naive_filter(scr, col_nums):
    def check_a_col(idx, num):
        return sum([l[idx] for l in scr]) == num

    return all(itertools.starmap(check_a_col, enumerate(col_nums)))


def main():
    m = 3
    cs = [ 1, 0, 0 ]
    ns = [ 0, 1, 0 ]

    lines = [generate_line(m, n) for n in ns]
    #lines = map(lambda k: generate_line(m, k), ns)

    # a = ['ab', '12', 'df']
    # print(list(itertools.product(*a)))

    res = [ s  for s in itertools.product(* lines)
            if naive_filter(s, cs) ]
    print(res)


if __name__ == '__main__':
    main()
