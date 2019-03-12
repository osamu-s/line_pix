#!/usr/bin/env python3

### generate perm

import itertools

def generate_line(size, nums):
    if len(nums) == 0:
        return [0]*size

    c_num = nums[0]
    lest_num = nums[1:]

    spcs = len(lest_num)
    lest_size = sum(lest_num) + spcs

    room = size - lest_size
    if room < c_num:
        print('error', size, room, lest_size, nums)
        return             ###
    return [ [0] *i + [1] * c_num
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
