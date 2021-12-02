# -*- coding: utf-8 -*-
"""
part1
"""

with open('input.txt') as f:
    contents = f.read().splitlines()
    

forward = [word for word in contents if 'forward' in word]
up = [word for word in contents if 'up' in word]
down = [word for word in contents if 'down' in word]

forward = [i.split(' ', 1)[1] for i in forward]
forward = [int(i) for i in forward]
x = sum(forward)

up = [i.split(' ', 1)[1] for i in up]
up = [int(i) for i in up]
down = [i.split(' ', 1)[1] for i in down]
down = [int(i) for i in down]

y = sum(down)-sum(up)

output = x*y


"""
part2
"""
direction =  [i.split(' ', 1)[0] for i in contents]
steps = [i.split(' ', 1)[1] for i in contents]
vertical = 0 
x = 0
y = 0

for i in range(len(contents)):
    if direction[i] == 'forward':
        x += int(steps[i])
        vertical += y*int(steps[i])
    elif direction[i] == 'down':
        y += int(steps[i])
    else :
        y -= int(steps[i])

output = x * vertical