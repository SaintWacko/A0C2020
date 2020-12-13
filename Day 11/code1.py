import os
import sys
import numpy as np
np.set_printoptions(threshold=sys.maxsize)


def main():
    lines = []
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input'), 'r') as file:
        lines = file.read().splitlines()
        lines = np.array([[{'L': 0, '.': None}[seat] for seat in line] for line in lines])
    # printSeats(np.copy(lines))
    while True:
        nextLines = step(lines)
        # printSeats(np.copy(nextLines))
        if (lines == nextLines).all():
            return sum(filter(None, lines.flatten()))
        lines = nextLines


def step(lines):
    nextLines = np.copy(lines)
    height = len(lines)
    width = len(lines[0])
    for (idy, idx), seat in np.ndenumerate(lines):
        adjacent = sum(filter(None, lines[max(idy - 1, 0):min(idy + 2, height), max(idx - 1, 0):min(idx + 2, width)].flatten()))
        if seat and adjacent >= 5:
            nextLines[idy][idx] = 0
        elif seat is not None and adjacent == 0:
            nextLines[idy][idx] = 1
    return nextLines


def printSeats(lines):
    for (idy, idx), seat in np.ndenumerate(lines):
        if seat == 1:
            lines[idy][idx] = '#'
        if seat is None:
            lines[idy][idx] = '.'
        if seat == 0:
            lines[idy][idx] = 'L'
    for line in lines:
        print(''.join(line))
    print()










if __name__ == "__main__":
    print(main())
