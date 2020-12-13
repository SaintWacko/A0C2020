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
    height = len(lines)
    width = len(lines[0])

    def checkDirections(idy, idx):
        visible = 0
        directions = [
            (-1, 0),
            (-1, 1),
            (0, 1),
            (1, 1),
            (1, 0),
            (1, -1),
            (0, -1),
            (-1, -1),
        ]
        for direction in directions:
            y = idy + direction[0]
            x = idx + direction[1]
            while 0 <= y < height and 0 <= x < width:
                if lines[y][x] is None:
                    y = y + direction[0]
                    x = x + direction[1]
                else:
                    if lines[y][x]:
                        visible += 1
                    break
                
        return visible

    nextLines = np.copy(lines)
    height = len(lines)
    width = len(lines[0])
    for (idy, idx), seat in np.ndenumerate(lines):
        visible = checkDirections(idy, idx)
        if seat and visible >= 5:
            nextLines[idy][idx] = 0
        elif seat is not None and visible == 0:
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
