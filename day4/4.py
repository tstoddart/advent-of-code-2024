# import the input as a matrix. Scan each row for occurrences of XMAS, rotate 90 degrees, ...
# use lists of lists or numpy matrix?

import sys
import numpy as np

with open(sys.argv[1]) as f:
    input = [list(l) for l in f.read().splitlines()]

class WordSearch():
    def __init__(self, inp):
        self.inp = inp

    def part1(self):
        count = 0

        for k in range(4):
            m = np.rot90(self.inp, k)

            for row in m:
                count += ''.join(row).count("XMAS")
            for j in range(-m.shape[0], m.shape[1]):
                count += ''.join(np.diagonal(m, offset=j)).count("STRING")

        return count

    def part2(self):
        count = 0
        arr_input = np.array(self.inp)

        for i, j in zip(*np.where(arr_input == 'A')):
            mi = arr_input[i-1:i+2, j-1:j+2]
            if self.__is_cross_mas_part2(mi):
                count += 1
        return count

    # helper func to check whether 3x3 submatrix is a valid X-MAS.
    def __is_cross_mas_part2(self, arr):
        # once the 3x3 matrix has been flattened into a 1d array, only the odd indices matter to
        # determine if this is a valid X-MAS, so make a subarray of just those elements.
        flat_arr = arr.flatten()[0::2]

        # there are four valid X-MASes corresponding to the rotations
        if ''.join(flat_arr) in [ "MSAMS", "SMASM", "MMASS", "SSAMM" ]:
            return True
        else:
            return False

if __name__ == "__main__":
    w = WordSearch(input)
    print("part 1 = ", w.part1())
    print("part 2 = ", w.part2())
