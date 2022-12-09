#!/usr/bin/env python

from sys import argv
from grid import Grid

VECTORS = {
    'U': (0, -1),
    'D': (0, 1),
    'L': (-1, 0),
    'R': (1, 0),
}

def new_tail_position(tail, head):
    dx = head[0] - tail[0]
    dy = head[1] - tail[1]
    new_x = tail[0]
    new_y = tail[1]
    if abs(dx) > 1 or abs(dy) > 1:
        if abs(dx) > 0:
            new_x += int(abs(dx) / dx)
        if abs(dy) > 0:
            new_y += int(abs(dy) / dy)
    return (new_x, new_y)

def part1(instructions):
    grid = Grid()
    head = (0, 0)
    tail = (0, 0)
    grid[tail] = '#'
    for instruction in instructions:
        (direction, count) = instruction
        count = int(count)
        vector = VECTORS[direction]
        #print(f"I: {instruction}")
        for _ in range(0, count):
            head = (head[0] + vector[0], head[1] + vector[1])
            #print(f"  H: {head}")
            tail = new_tail_position(tail, head)
            #print(f"  T: {tail}")
            grid[tail] = '#'
            #print(f"{grid}")
    visited = grid.places
    print(f"{len(visited)} positions visited")


def part2(instructions):
    knots = [(0,0)] * 10
    grid = Grid()
    for instruction in instructions:
        (direction, count) = instruction
        count = int(count)
        vector = VECTORS[direction]
        #print(f"I: {instruction}")
        for _ in range(0, count):
            knots[0] = (knots[0][0] + vector[0], knots[0][1] + vector[1])
            for i in range(1,10):
                knots[i] = new_tail_position(knots[i], knots[i-1])
            grid[knots[9]] = '9'

        #tmp = Grid()
        #tmp[(0,0)] = 's'
        #for i in range(0,10):
        #    tmp[knots[i]] = chr(ord('0') + i)
        #print(f"{tmp}")
    visited = grid.places
    print(f"{len(visited)} positions visited")
    

instructions = [line.strip().split(' ') for line in open(argv[1], 'r').readlines()]

part1(instructions)
part2(instructions)
   
