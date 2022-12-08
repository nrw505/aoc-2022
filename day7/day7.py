#!/usr/bin/env python

from sys import argv

class Dir:
    def __init__(self, parent, name):
        self.entries = {}
        self.parent = parent
        self.name = name

    def entry(self, path):
        return self.entries[path]

    def add(self, path, item):
        self.entries[path] = item

    def totalsize(self):
        return sum([e.totalsize() for e in self.entries.values()])

    def directories(self):
        dirs = []
        for entry in self.entries.values():
            if isinstance(entry, Dir):
                dirs += entry.directories()
        dirs += [self]
        return dirs

class File:
    def __init__(self, size, name):
        self.size = size
        self.name = name

    def totalsize(self):
        return self.size

def construct_tree(input):
    root = Dir(None, '/')
    pwd = root
    for line in input.readlines():
        line = line.strip()
        if line == '$ cd /':
            pwd = root
        elif line == '$ cd ..':
            pwd = pwd.parent
        elif line.startswith('$ cd '):
            newdir = line[5:]
            pwd = pwd.entry(newdir)
        elif line.startswith('$ '):
            # skip all unrecognized commands
            # including LS which we don't need to care about right now
            pass
        elif line.startswith('dir '):
            # it's a directory from a ls command
            path = line[4:]
            pwd.add(path, Dir(pwd, path))
        else:
            # it's a file from a ls command
            (size, path) = line.split(' ')
            pwd.add(path, File(int(size), path))
    return root

input = open(argv[1], "r")
tree = construct_tree(input)

# Part1

sizes = [each.totalsize() for each in tree.directories()]
total = sum([size for size in sizes if size <= 100000])

print(f"total size sum = {total}")

# Part2

disk_size = 70000000
needed_free = 30000000

free_space_now = disk_size - tree.totalsize()
to_free = needed_free - free_space_now

smallest_sufficient = min([size for size in sizes if size >= to_free])

print(f"smallest to delete = {smallest_sufficient}")
