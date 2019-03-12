#!/usr/bin/env python3

### generate perm

import itertools

def generate_line(size, nums):

    req_size = sum(num) + (len(nums) -1)
    box_lst = range(len(nums) +1)
    float_spc = size - req_size

    spc_dist = itertools.combinations_with_replacement(box_lst, float_spc)

    return [ [0] *i + [1] * c_num +[0]
             + generate_line(size - c_num -1 -i, lest_num)
            for i in range(room - c_num + 1) ]

def main():
    m = 5
    #cs = [[5], [1,1,1], [ 1, 2 ], [2, 1]]
    cs = [[5], [1,1,1], [ 1, 2 ]]

    lines = [generate_line(m, n) for n in cs]
    print(lines)

    # a = ['ab', '12', 'df']
    # print(list(itertools.product(*a)))



if __name__ == '__main__':
    main()
