#import numpy as np
with open('input.txt') as f:
        lines = f.read().splitlines()

full_list = [ int(x) for xs in [i.split() for i in lines] for x in xs  ]
list1 = sorted(full_list[1::2])
list2 = sorted(full_list[0::2])

part1 = sum([abs(x) for x in map(int.__sub__, list1, list2)])
part2 = sum([x*list2.count(x) for x in list1])

print("part 1 =", part1)
print("part 2 =", part2)
