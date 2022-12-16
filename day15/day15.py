#!/usr/bin/env python

from sys import argv
from grid import Grid
import re

SENSOR_RE = re.compile('Sensor at x=([0-9-]*), y=([0-9-]*): closest beacon is at x=([0-9-]*), y=([0-9-]*)')

def read_sensors(input):
    sensors = []
    for line in input.readlines():
        match = SENSOR_RE.match(line)
        if match:
            (sensor_x, sensor_y, beacon_x, beacon_y) = [int(x) for x in match.groups()]
            sensors.append(((sensor_x, sensor_y), (beacon_x, beacon_y)))
    return sensors

def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def columns_excluded(sensor, beacon, row):
    dist = manhattan_distance(sensor, beacon)
    y_dist = abs(row - sensor[1])
    x_dist = dist - y_dist
    return set(range(sensor[0] - x_dist, sensor[0] + x_dist + 1))

def part1(sensors, row):
    excluded = set()
    for sensor, beacon in sensors:
        this_set = columns_excluded(sensor, beacon, row)
        # print(f"sensor @ {sensor}, beacon @ {beacon}: {this_set} excluded")
        excluded.update(this_set)
    # remove the coordinates of the beacons, they don't count as
    # places that a beacon cannot be
    for _, beacon in sensors:
        if beacon[1] == row and beacon[0] in excluded:
            excluded.remove(beacon[0])
    print(f"{len(excluded)} positions where a beacon cannot be present")

def x_range_excluded(sensor, beacon, y):
    dist = manhattan_distance(sensor, beacon)
    y_dist = abs(y - sensor[1])
    x_dist = dist - y_dist
    if x_dist < 0:
        return None
    return (sensor[0] - x_dist, sensor[0] + x_dist)

def merge_ranges(ranges):
    if not ranges:
        return []
    # Sort the input ranges: default sort order will sort in order of
    # increasing left-hand-side
    ranges = sorted(ranges)
    current = [ranges[0][0], ranges[0][1]]
    new_ranges = [current]
    for i in range(1, len(ranges)):
        test = ranges[i]
        # If we overlap _or adjoin_ and the new one's right-hand-side is bigger, extend
        if test[0] <= (current[1] + 1) and test[1] > current[1]:
            current[1] = test[1]
        # If we don't overlap _or adjoin_, make a new current
        if test[0] > (current[1] + 1):
            current = [test[0], test[1]]
            new_ranges.append(current)
    return new_ranges

def part1_faster(sensors, row):
    ranges_excluded = [r for r in [x_range_excluded(sensor, beacon, row) for sensor, beacon in sensors] if r]
    merged = merge_ranges(ranges_excluded)
    counts = [r[1] - r[0] for r in merged]
    print(f"{sum(counts)} positions where a beacon cannot be present")
    
def part2(sensors, min_coord, max_coord):
    y = 0
    while y <= max_coord:
        ranges_excluded = [r for r in [x_range_excluded(sensor, beacon, y) for sensor, beacon in sensors] if r]
        merged = merge_ranges(ranges_excluded)
        if len(merged) > 1:
            # according to the problem description there will only be
            # one possibly point, so this is messy
            x = merged[0][1] + 1
            code = x * 4000000 + y
            print(f"x={x}, y={y}, code={code}")

        #left_extend = abs(min_coord - merged[0][0])
        #right_extend = merged[0][1] - max_coord
        #skip = min(left_extend, right_extend)
        #skip = max(skip, 0)
        #if skip > 0:
        #    print(f"y={y}, skip={skip}")
        skip = 0
        y += 1 + skip
        

input = open(argv[1], 'r')
sensors = read_sensors(input)

row = int(argv[2])
max_coord = int(argv[3])

part1(sensors, row)
part1_faster(sensors, row)
part2(sensors, 0, max_coord)
