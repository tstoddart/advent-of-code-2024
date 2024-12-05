
import sys

with open(sys.argv[1]) as f:
    input = [l for l in f.read().splitlines()]

class Rule():
    def __init__(self, str):
        self.l = [*map(int, str.split('|'))]

    def isvalid(self, update):
        first = False

        # if all(i in update for i in self.l):
        if set(self.l).issubset(set(update)):
            if update.index(self.l[1]) > update.index(self.l[0]):
                return True
            else:
                return False
        else:
            return True

def parse_rules_and_updates(inp):
    brk = inp.index('') # the blank line separates the updates from the rules

    rules = [ Rule(r) for r in inp[0:brk-1] ]
    updates = [ [ int(i) for i in x.split(',') ] for x in inp[brk+1:] ]

    return rules, updates

def part1(rules, updates):
    sum = 0
    for u in updates:
        valid = True

        for i, r in enumerate(rules):
            if not r.isvalid(u):
                valid = False
                continue

        if valid:
            sum += u[len(u)//2] # add the middle element to the sum

    return sum

def part2(rules, updates):
    sum = 0
    for u in updates:
        while True:
            swaps = 0
            for i, r in enumerate(rules):
                if not r.isvalid(u):
                    # reverse the order of the elements of the rule
                    u[u.index(r.l[0])], u[u.index(r.l[1])] = r.l[1], r.l[0]
                    swaps+=1

            # if there are no swaps then this update is valid against all the rules and we can break the loop
            if swaps == 0:
                break
            elif swaps > 10000: # backstop to break the loop
                break

        sum += u[len(u)//2]

    return sum

if __name__ == "__main__":
    rules, updates = parse_rules_and_updates(input)

    part1 = part1(rules, updates)

    # part2 asks for the sums of just the re-ordered rules, the easiest way to
    # programme this is just to subtract the result for part1
    part2 = part2(rules, updates) - part1

    print('part 1 = ', part1)
    print('part 2 = ', part2)
