from itertools import groupby


class SecureContainer:
    def __init__(self, num_range, part2=False):
        self.cur_num = 0
        self.num_range = num_range
        self.total_possibilities = []
        self.part2 = part2
        self.part2_criteria_met = False

    def count_possibilities(self):
        for i in self.num_range:
            self.cur_num = i
            self.part2_criteria_met = False
            if not self.has_repeating_chars():
                # print(f"{self.cur_num}: no repeating chars!")
                continue

            if not self.nums_never_decrease():
                # print(f"{self.cur_num}: Numbers decrease left to right!")
                continue

            if (self.part2 is True) & (self.part2_criteria_met is False):
                print(f"{self.cur_num}: Does not meet part 2 criteria!")
                continue

            self.total_possibilities.append(i)

    def has_repeating_chars(self):
        has_repeating_chars = False
        repeating_chars = [list(g) for k, g in groupby(str(self.cur_num))]
        for g in repeating_chars:
            if (len(g)) > 1:
                has_repeating_chars = True
                if self.part2 is True:
                    if (len(g)) == 2:
                        self.part2_criteria_met = True
                        break
                else:
                    break

        return has_repeating_chars

    def nums_never_decrease(self):
        res = True
        last_num = 0
        for n in str(self.cur_num):
            if int(n) < last_num:
                res = False
                break
            last_num = int(n)

        return res


s = SecureContainer(range(236491, 713788, 1))
s.count_possibilities()
print("{0} are possible".format(len(s.total_possibilities)))

p2 = SecureContainer(range(236491, 713788, 1), True)
p2.count_possibilities()
print("{0} are possible for part2".format(len(p2.total_possibilities)))
