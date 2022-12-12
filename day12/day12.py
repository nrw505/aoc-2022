#!/usr/bin/env python

from sys import argv
from grid import Grid
from functools import reduce
from operator import iconcat

DIRECTIONS = [
    (1, 0), # east
    (-1, 0), # west
    (0, 1), # south
    (0, -1), # north
]

def height(grid, position):
    c = grid[position]
    if c == 'S':
        return ord('a')
    if c == 'E':
        return ord('z')
    return ord(c)

def neighbours(grid, position):
    positions = [(position[0] + d[0], position[1] + d[1]) for d in DIRECTIONS]
    return [position for position in positions if position in grid]

def possible_entrances(grid, position):
    my_height = height(grid, position)
    return [
        n for n in neighbours(grid, position)
        if height(grid, n) + 1 >= my_height
    ]

def possible_exits(grid, position):
    my_height = height(grid, position)
    return [
        n for n in neighbours(grid, position)
        if height(grid, n) <= my_height + 1
    ]

input = open(argv[1], 'r')

grid = Grid()
grid.read_from(input)

end = [place for place in grid.places if grid[place] == 'E'][0]
start = [place for place in grid.places if grid[place] == 'S'][0]

def part1(grid, end, start):
    # tmp = Grid()
    i = 0
    active = [start]
    visited = set(active)
    while end not in active:
        # for pos in active:
        #     tmp[pos] = chr(i + ord('0'))
        # print(f"iteration {i}")
        # print(f"{len(active)} in active")
        # print(f"{len(visited)} in visited")
        # print(f"{tmp}")
        # print("")
        step = set(reduce(iconcat, [[n for n in possible_exits(grid, pos) if n not in visited] for pos in active]))
        visited.update(step)
        active = step
        i += 1
    
    print(f"{i} steps to end")


def part2(grid, end):
    i = 0
    active = [end]
    visited = set(active)
    while not any([grid[pos] == 'a' for pos in active]):
        step = set(reduce(iconcat, [[n for n in possible_entrances(grid, pos) if n not in visited] for pos in active]))
        visited.update(step)
        active = step
        i += 1

    print(f"{i} steps to elevation a")
        

part1(grid, end, start)
part2(grid, end)
