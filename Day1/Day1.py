# -*- coding: utf-8 -*-
"""
part1
"""

with open('Input.txt') as f:
    contents = f.read().splitlines()

dif = [int(l2) - int(l1) for l1, l2 in zip(contents, contents[1:])]
only_pos = [num for num in dif if num > 0]
pos_count = len(only_pos)
print(pos_count)


"""
part2
"""

sliding = [int(l1) + int(l2) + int(l3) for l1, l2, l3 in zip(contents, contents[1:], contents[2:])]
dif = [int(l2) - int(l1) for l1, l2 in zip(sliding, sliding[1:])]
only_pos = [num for num in dif if num > 0]
pos_count = len(only_pos)
print(pos_count)