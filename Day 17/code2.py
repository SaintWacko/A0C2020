import os
import sys
import numpy as np
np.set_printoptions(threshold=sys.maxsize)

CYCLES = 6


def main():
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input'), 'r') as file:
        lines = [[int(num) for num in list(line.replace('#', '1').replace('.', '0'))] for line in file.read().splitlines()]
        dim = np.array([[lines]])
        for i in range(CYCLES):
            dim = step(dim)
            print(sum(dim.flatten()))
        return sum(dim.flatten())


def step(dim):
    dim = np.pad(dim, ((1, 1), (1, 1), (1, 1), (1, 1)), 'constant')
    nextDim = np.copy(dim)
    z = len(dim)
    y = len(dim[0])
    x = len(dim[0][0])
    w = len(dim[0][0][0])
    for (idz, idy, idx, idw), cube in np.ndenumerate(dim):
        adjacent = sum(dim[
            max(idz - 1, 0):min(idz + 2, z),
            max(idy - 1, 0):min(idy + 2, y),
            max(idx - 1, 0):min(idx + 2, x),
            max(idw - 1, 0):min(idw + 2, w), ].flatten())
        if cube:
            if not (3 <= adjacent <= 4):
                nextDim[idz][idy][idx][idw] = 0
        else:
            if adjacent == 3:
                nextDim[idz][idy][idx][idw] = 1
    return nextDim


if __name__ == "__main__":
    print(main())
