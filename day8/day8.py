#!/usr/bin/env python

import sys

from grid import Grid

infile = open(sys.argv[1])

trees = Grid()
trees.read_from(infile)

def is_visible(trees, position):
    (my_x, my_y) = position
    east_positions = [(x, my_y) for x in range(0, my_x)]
    west_positions = [(x, my_y) for x in range(my_x + 1, trees.max_x() + 1)]
    north_positions = [(my_x, y) for y in range(0, my_y)]
    south_positions = [(my_x, y) for y in range(my_y + 1, trees.max_y() + 1)]
    if all([int(trees[other]) < int(trees[position]) for other in west_positions]) or not east_positions:
        return True
    if all([int(trees[other]) < int(trees[position]) for other in east_positions]) or not west_positions:
        return True
    if all([int(trees[other]) < int(trees[position]) for other in north_positions]) or not north_positions:
        return True
    if all([int(trees[other]) < int(trees[position]) for other in south_positions]) or not south_positions:
        return True
    return False

def trees_visible(trees, position, direction):
    max_x = trees.max_x()
    max_y = trees.max_y()
    min_x = trees.min_x()
    min_y = trees.min_y()
    my_height = int(trees[position])

    x = position[0] + direction[0]
    y = position[1] + direction[1]
    visible = 0
    while x >= min_x and x <= max_x and y >= min_y and y <= max_y:
        visible += 1
        if int(trees[(x, y)]) < my_height:
            x += direction[0]
            y += direction[1]
        else:
            # stop looking, we can't look any further
            x = min_x - 1
            y = min_y - 1
    return visible

def visibility_score(trees, position):
    (my_x, my_y) = position

    v_west = trees_visible(trees, position, (-1, 0))
    v_east = trees_visible(trees, position, (1, 0))
    v_north = trees_visible(trees, position, (0, -1))
    v_south = trees_visible(trees, position, (0, 1))

    return v_west * v_east * v_north * v_south

def part1(trees):
    visible = 0
    for position in trees.places:
        if is_visible(trees, position):
            visible += 1
    print(f"{visible} trees visible")

def part2(trees):
    best_score = 0
    for position in trees.places:
        score = visibility_score(trees, position)
        if score > best_score:
            best_score = score
    print(f"best scenic score is {best_score}")


part1(trees)
part2(trees)
