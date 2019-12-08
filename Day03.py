import matplotlib.pyplot as plt


def line_intersects(seg1, seg2):
    x1 = seg1[0][0]
    y1 = seg1[0][1]

    x2 = seg1[1][0]
    y2 = seg1[1][1]

    x3 = seg2[0][0]
    y3 = seg2[0][1]

    x4 = seg2[1][0]
    y4 = seg2[1][1]

    if x3 in range(min(x1, x2), max(x1, x2)):
        print(f"{x3} is in range!")
    return False


def get_segments(coords):
    segments = {}
    for i in range(0, len(coords) - 1, 1):
        seg = [coords[i], coords[i + 1]]
        segments[f"{i}"] = seg

    return segments


class CrossedWires:

    def __init__(self):
        self.line1_segments = []
        self.lines_storage = [l.split(',') for l in open("Day03_input.txt", "r").readlines()]
        self.lines = self.lines_storage[:]
        self.line = [{"points": []}, {"points": []}]
        self.calculating = True
        self.get_line_coords(0)
        self.get_line_coords(1)
        self.intersections = set(self.line[0]["points"]) & set(self.line[1]["points"])

    def part1(self):
        plt.plot(*zip(*self.line[0]["points"]), color='b', label="Line1")
        plt.plot(*zip(*self.line[1]["points"]), color='k', label="Line2")
        plt.scatter(*zip(*self.intersections), color='r', label="intersections ({0})".format(len(self.intersections)))
        min_man_d = 99999999999999999
        for p in self.intersections:
            x, y = p
            plt.scatter(x, y)
            # Annotate the Manhattan Distance
            man_d = abs(x) + abs(y)
            if(man_d < min_man_d) & (man_d > 0):
                min_man_d = man_d
                min_man_d_pt = p
        # Plot the point with lowest man_d
        plt.annotate(f"winner! {min_man_d} {min_man_d_pt}", min_man_d_pt)
        plt.legend()
        plt.show()

    def part2(self):
        points = [0, 1]
        tot_points = [0, 1]
        min_total_points = 9999999999
        for i in self.intersections:
            if i != (0, 0):
                for idx in range(0, 2, 1):
                    points[idx] = 0
                    for p in self.line[idx]["points"]:
                        if p != (0, 0):
                            points[idx] = points[idx] + 1
                            if p == i:
                                print("points until intersection line {2} {0} : {1}".format(p, points[idx], idx))
                                tot_points[idx] = points[idx]
                                break
                if tot_points[0] + tot_points[1] < min_total_points:
                    min_total_points = tot_points[0] + tot_points[1]
                    min_intersection = i
        print(self.intersections)
        print(f"Min intersection: {min_intersection} with {min_total_points} points")

    def get_line_coords(self, line_idx):
        line = self.lines[line_idx]
        initial_coords = 0, 0
        self.line[line_idx]["points"].append(initial_coords)
        for p in line:
            self.get_next_coord(self.line[line_idx]["points"][-1], p, line_idx)

    def get_next_coord(self, position, point, line_idx, interval=1):
        d = point[0]
        magnitude = int(point[1:])

        x = position[0]
        y = position[1]

        new_coord = x, y

        # self.line[line_idx]["points"].append(new_coord)

        for m in range(interval, magnitude + 1, interval):
            if d == "U":
                y += interval

            if d == 'D':
                y = y - interval

            if d == 'R':
                x += interval

            if d == 'L':
                x -= interval

            new_coord = x, y

            self.line[line_idx]["points"].append(new_coord)


if __name__ == '__main__':
    c = CrossedWires()
    c.part1()
    c.part2()

# (-156, -137)
