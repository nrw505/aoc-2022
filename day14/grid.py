class Grid:
    def __init__(self, default=" "):
        self.default = default
        self.places = {(0, 0): self.default}

    def copy(self):
        new = Grid(self.default)
        new.clear(0, 0)
        for place in self.places:
            new[place] = self[place]
        return new

    def put(self, x, y, tile):
        self.places[(x, y)] = tile

    def get(self, x, y):
        return self.places[(x, y)]

    def clear(self, x, y):
        del self.places[(x, y)]

    def validate_pos(self, pos):
        if len(pos) != 2:
            raise TypeError("Bad position")

    def __setitem__(self, pos, tile):
        # so ``grid[(x, y)] = '*'`` works
        self.validate_pos(pos)
        self.places[pos] = tile

    def __getitem__(self, pos):
        # so ``tile = grid[(x, y)]`` works
        self.validate_pos(pos)
        return self.places[pos]

    def __delitem__(self, pos):
        self.validate_pos(pos)
        del self.places[pos]

    def __len__(self):
        return len(self.places)

    def __contains__(self, pos):
        self.validate_pos(pos)
        return pos in self.places

    def min_x(self):
        return min([pos[0] for pos in self.places])

    def max_x(self):
        return max([pos[0] for pos in self.places])

    def min_y(self):
        return min([pos[1] for pos in self.places])

    def max_y(self):
        return max([pos[1] for pos in self.places])

    def read_from(self, file):
        y = 0
        for line in file:
            line = line.strip("\n")
            x = 0
            for c in line:
                self[(x, y)] = c
                x += 1
            y += 1

    def __str__(self):
        origin_x = -self.min_x()
        origin_y = -self.min_y()

        width = self.max_x() - self.min_x() + 1
        height = self.max_y() - self.min_y() + 1

        canvas = []
        for _y in range(height):
            canvas.append([self.default] * width)

        for place in self.places:
            canvas[origin_y + place[1]][origin_x + place[0]] = self.places[place]

        return "\n".join(["".join(line) for line in canvas])
        
    def print(self):
        print(str(self))
