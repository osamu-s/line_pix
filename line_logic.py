#!/usr/bin/env python3

### generate perm

from itertools import chain, zip_longest, combinations_with_replacement

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

    req_size = sum(nums) + (len(nums) -1)
    float_spc = size - req_size
    box_idxs = range(len(nums) +1)

    blank_rl_base = [0] + [1] * (len(nums)-1) + [0]
    blank_rls = (mk_blank_rl(blank_rl_base.copy(), list(idx))
                 for idx in combinations_with_replacement(box_idxs, float_spc) )

    return [ list(render(brl, nums)) for brl in blank_rls ]

def main():
    m = 5
    cs = [[5], [1,1,1], [ 1, 2 ], [2, 1]]

    lines = [generate_line(m, n) for n in cs]
    print(lines)

    print(decided_dot_in_line(lines))

    # a = ['ab', '12', 'df']
    # print(list(itertools.product(*a)))



if __name__ == '__main__':
    main()
