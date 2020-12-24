import os
import sys
import numpy as np
np.set_printoptions(threshold=sys.maxsize, linewidth=sys.maxsize)

dirmap = {
    'nw': (-1, 0),
    'ne': (-1, 1),
    'e': (0, 1),
    'se': (1, 0),
    'sw': (1, -1),
    'w': (0, -1),
}


def step(grid):
    nextGrid = np.copy(grid)
    y = len(grid)
    x = len(grid[0])
    for (idy, idx), tile in np.ndenumerate(grid):
        adjacent = sum(grid[
            max(idy - 1, 0):min(idy + 1, y),
            max(idx, 0):min(idx + 2, x)].flatten())
        adjacent += sum(grid[
            max(idy, 0):min(idy + 2, y),
            max(idx - 1, 0):min(idx + 1, x)].flatten())
        if tile:
            # print(adjacent)
            if adjacent == 2 or adjacent > 4:
                nextGrid[idy][idx] = 0
        else:
            if adjacent == 2:
                nextGrid[idy][idx] = 1
    return nextGrid


def main():
    paths = []
    tiles = []
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input'), 'r') as file:
        lines = file.read().splitlines()
        for line in lines:
            path = []
            iLine = iter(line)
            for d in iLine:
                if d in ['n', 's']:
                    path.append(d + next(iLine))
                else:
                    path.append(d)
            paths.append(path)
    # print(paths)
    for path in paths:
        y = 0
        x = 0
        for dir in path:
            dy, dx = dirmap[dir]
            y += dy
            x += dx
        tile = (y, x)
        if tile in tiles:
            tiles.remove(tile)
        else:
            tiles.append(tile)
    # print(tiles)
    size = 140
    grid = np.zeros((size, size))
    for tile in tiles:
        y, x = tile
        grid[y + int(size / 2)][x + int(size / 2)] = 1
    for _ in range(100):
        grid = step(grid)
        # print(int(sum(grid.flatten())))
    # print(grid)
    return int(sum(grid.flatten()))







if __name__ == "__main__":
    print(main())


# cancel out pairs of se/nw ne/sw