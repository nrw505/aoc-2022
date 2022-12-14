#!/usr/bin/env python

from sys import argv
from grid import Grid

def draw_line(grid, symbol, start, end):
    pos = start
    grid[pos] = symbol
    while pos != end:
        dx = end[0] - pos[0]
        dy = end[1] - pos[1]
        new_x = pos[0]
        new_y = pos[1]
        if abs(dx) > 0:
            new_x += int(abs(dx) / dx)
        if abs(dy) > 0:
            new_y += int(abs(dy) / dy)
        pos = (new_x, new_y)
        grid[pos] = symbol

def sand_destination(grid, sand, abyss_y):
    if sand[1] > abyss_y:
        return None

    possible_locations = [
        (sand[0], sand[1] + 1), # down
        (sand[0] - 1, sand[1] + 1), # down, left
        (sand[0] + 1, sand[1] + 1), # down, right
    ]
    for next_pos in possible_locations:
        if next_pos not in grid:
            return sand_destination(grid, next_pos, abyss_y)
    return sand

input = open(argv[1], 'r')

grid = Grid()
for line in input.readlines():
    line = line.strip()
    coordinates = [tuple([int(x) for x in coordinate.split(',')]) for coordinate in line.split(' -> ')]
    for i in range(1, len(coordinates)):
        start = coordinates[i-1]
        end = coordinates[i]
        draw_line(grid, '#', start, end)

grid.clear(0,0)
sand_source = (500, 0)
grid[sand_source] = '+'

#print("starting grid")
#grid.print()

def part1(grid, sand_source):
    abyss_y = grid.max_y()

    i = 0
    sand = sand_destination(grid, sand_source, abyss_y)
    while sand:
        i += 1
        grid[sand] = 'o'
        #print(f"iteration {i}")
        #grid.print()
        sand = sand_destination(grid, sand_source, abyss_y)

    print(f"{i} sand until abyss")

def part2(grid, sand_source):
    floor_y = grid.max_y() + 2
    draw_line(grid, '#', (500 - (floor_y + 1), floor_y), (500 + (floor_y + 1), floor_y))

    i = 0
    sand = sand_destination(grid, sand_source, floor_y+1)
    while sand and grid[sand_source] == '+':
        i += 1
        grid[sand] = 'o'
        #print(f"iteration {i}")
        #grid.print()
        sand = sand_destination(grid, sand_source, floor_y+1)

    print(f"{i} sand until full")
    
part1(grid.copy(), sand_source)
part2(grid.copy(), sand_source)
