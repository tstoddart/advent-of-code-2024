import sys

class Report():
    def __init__(self, levels, dampener=True):
        self.levels = levels
        self.dampener = dampener

    def isvalid(self):
        if not self.dampener:
            if self.differences_less_than_n(3) and (self.strictly_increasing() or self.strictly_decreasing()):
                return True
            else:
                return False
        elif self.dampener:
            # make a list of all of the possible dampened reports for this report 
            dampened_reports = [exclude(self.levels, x) for x in range(len(self.levels))]
            # iterate through each of the dampened reports and see if any of them are valid
            for i in dampened_reports:
                r = Report(i, dampener=False)
                if r.isvalid():
                    return True

    def strictly_increasing(self):
        return all(x<y for x, y in zip(self.levels, self.levels[1:]))

    def strictly_decreasing(self):
        return all(x>y for x, y in zip(self.levels, self.levels[1:]))

    def differences_less_than_n(self, n):
        return all(abs(x-y)<=n for x, y in zip(self.levels, self.levels[1:]))

# return a list excluding the ith element of lst without modifying lst
def exclude(lst, i):
        return lst[:i] + lst[i + 1:]

if __name__ = "__main__":
    with open(sys.argv[1]) as f:
        lines = [list(map(int, l.split())) for l in f.read().splitlines()]

    count = 0
    for line in lines:
        r = Report(line)
        if r.isvalid():
            count += 1

    print(count)
