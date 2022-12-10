#!/usr/bin/env python

from sys import argv
from grid import Grid
from math import floor

x_per_cycle = [1]

instructions = [line.strip() for line in open(argv[1], 'r').readlines()]

for instruction in instructions:
    if instruction == 'noop':
        x_per_cycle.append(x_per_cycle[-1])
    if instruction.startswith('addx '):
        amount = int(instruction.split(' ')[1])
        x_per_cycle.append(x_per_cycle[-1])
        x_per_cycle.append(x_per_cycle[-1] + amount)
        

# print(f"x_per_cycle: {x_per_cycle}")

sample_cycles = [19, 59, 99, 139, 179, 219]

samples = [x_per_cycle[cycle] for cycle in sample_cycles]

print(f"samples = {samples}")
signal_strenths = [x_per_cycle[cycle] * (cycle+1) for cycle in sample_cycles]
total = sum(signal_strenths)

print(f"total signal strenths = {total}")

crt = Grid()
for cycle in range(0, 240):
    column = cycle % 40
    row = int(floor(cycle/40))
    sprite_center = x_per_cycle[cycle]
    pixel = '.'
    if abs(column - sprite_center) < 2:
        pixel = '#'
    crt[(column, row)] = pixel

print(crt)
