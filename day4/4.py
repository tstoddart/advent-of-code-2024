# import the input as a matrix. Scan each row for occurrences of XMAS, rotate 90 degrees, ...
# use lists of lists or numpy matrix?

import sys
import numpy as np

with open(sys.argv[1]) as f:
    input = [list(l) for l in f.read().splitlines()]

class WordSearch():
    def __init__(self, inp):
        self.inp = inp

    # count the total occurrences of XMAS in the wordsearch.
    # 
    # rotate the input matrix through 90 degrees and each time and count the
    # occurrences of XMAS on each row and each diagonal. This covers both the
    # forward (XMAS) and backwards (SAMX) occurrences.
    def get_count_part1(self):
        count = 0

        # look at the matrix in each of 4 rotations...
        for k in range(4):
            m = np.rot90(self.inp, k)
            count += self.__count_xmas_in_matrix_part1(m, "XMAS")

        return count

    # helper function to count the occurrences of XMAS in a matrix, from
    # left to right, on rows and diagonals.
    def __count_xmas_in_matrix_part1(self, m, string):
        count = 0

        # count the occurrences of `string` in each row 
        for row in m:
            count += ''.join(row).count(string)

        # count the occurences of `string` for all the diagonals in the matrix
        for j in range(-m.shape[0], m.shape[1]):
            count += ''.join(np.diagonal(m, offset=j)).count(string)
        
        return count

    # count the total valid X-MASes in the input matrix
    def get_count_part2(self):
        count = 0
        arr_input = np.array(self.inp)

        # scan through the input matrix moving a 3x3 window from top left to bottom right
        for iy, ix in np.ndindex(np.array(self.inp).shape):
            mi = arr_input[ix:ix+3, iy:iy+3]

            # only look for x-mas if we haven't got to the end and add the check for the middle
            # string being 'A' as an easy optimisation
            if mi.shape == (3,3) and mi[1,1] == 'A':
                if self.__is_cross_mas_part2(mi):
                    count += 1
        return count

    # checks whether a 3x3 submatrix is a valid X-MAS.
    def __is_cross_mas_part2(self, arr):
        # once the 3x3 matrix has been flattened into a 1d array, only the odd indices matter to
        # determine if this is a valid X-MAS, so make a subarray of just those elements.
        flat_arr = arr.flatten()[0::2]

        # compare the flattened, 'compressed' array with the four valid X-MASes (corresponding to the rotations).
        if list(flat_arr) in [ list("MSAMS"), list("SMASM"), list("MMASS"), list("SSAMM") ]:
            return True
        else:
            return False

if __name__ == "__main__":
    w = WordSearch(input)
    print("part 1 = ", w.get_count_part1())
    print("part 2 = ", w.get_count_part2())
