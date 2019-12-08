from itertools import groupby


class SecureContainer:
    def __init__(self, num_range):
        self.cur_num = 0
        self.num_range = num_range
        self.total_possibilities = []

    def count_possibilities(self):
        for i in self.num_range:
            self.cur_num = i
            if not self.has_repeating_chars():
                print(f"{self.cur_num}: no repeating chars!")
                continue

            if not self.nums_never_decrease():
                print(f"{self.cur_num}: Numbers decrease left to right!")
                continue

            self.total_possibilities.append(i)

    def has_repeating_chars(self):
        has_repeating_chars = False
        repeating_chars = [list(g) for k, g in groupby(str(self.cur_num))]
        for g in repeating_chars:
            if (len(g)) > 1:
                has_repeating_chars = True
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
