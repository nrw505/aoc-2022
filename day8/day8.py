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

def visibility_score(trees, position):
    (my_x, my_y) = position
    my_height = int(trees[position])
    max_x = trees.max_x()
    max_y = trees.max_y()
    v_west = 0
    v_east = 0
    v_north = 0
    v_south = 0

    # look west
    x = my_x - 1
    y = my_y 
    while x >= 0:
        
        v_west += 1
        if int(trees[(x, y)]) < my_height:
            # look one further west
            x -= 1
        else:
            # skip to the end
            x = -1

    # look east
    x = my_x + 1
    y = my_y 
    while x <= max_x:
        v_east += 1
        if int(trees[(x, y)]) < my_height:
            # look one further east
            x += 1
        else:
            # skip to the end
            x = max_x + 1

    # look north
    x = my_x
    y = my_y - 1
    while y >= 0:
        v_north += 1
        if int(trees[(x, y)]) < my_height:
            # look one further west
            y -= 1
        else:
            # skip to the end
            y = -1

    # look south
    x = my_x
    y = my_y + 1 
    while y <= max_y:
        v_south += 1
        if int(trees[(x, y)]) < my_height:
            # look one further east
            y += 1
        else:
            # skip to the end
            y = max_y + 1

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
