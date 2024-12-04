import sys
import re
from math import prod

class Mul():
    def __init__(self, string):
        if "mul" in string:
            self.result = prod(map(int, string.removeprefix("mul(").removesuffix(")").split(",")))

    def result(self):
        return self.result

with open(sys.argv[1]) as f:
    input = f.read()

matches = re.findall(r"(mul\([0-9]+,[0-9]+\)|do\(\)|don't\(\))", input)

sum_part1 = 0
sum_part2 = 0
switch = True

for m in matches:
    if "do()" in m:
        switch = True
    elif "don't()" in m:
        switch = False
    elif "mul" in m:
        sum_part1 += Mul(m).result
        if switch is True:
            sum_part2 += Mul(m).result

print("part1 = ", sum_part1)
print("part2 = ", sum_part2)
