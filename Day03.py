import matplotlib.pyplot as plt
import pandas as pd


def get_next_coord(position, point):
    d = point[0]
    m = int(point[1:])

    x = position[0]
    y = position[1]

    if d == "U":
        y += m

    if d == 'D':
        y -= m

    if d == 'R':
        x += m

    if d == 'L':
        x -= m

    return x, y


def get_line_coords(line):
    coords = [(0, 0)]
    for p in line:
        coords.append(get_next_coord(coords[-1], p))

    return coords


class CrossedWires:

    def __init__(self):
        self.lines_storage = [l.split(',') for l in open("Day03_input.txt", "r").readlines()]
        self.lines = self.lines_storage[:]
        self.calculating = True

    def run(self):

        plt.plot(*zip(*get_line_coords(self.lines[0])), color='b', label="Line1")
        plt.plot(*zip(*get_line_coords(self.lines[1])), color='k', label="Line2")
        plt.legend()
        plt.show()


if __name__ == '__main__':
    c = CrossedWires()
    c.run()

# (-156, -137)
