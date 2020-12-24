import os
import numpy as np


class Image():
    # [B, L, T, R]

    def __init__(self, id, image):
        self.id = id
        self.edges = []
        self.neighbors = [None, None, None, None]
        self.grid = np.array(image)
        self.reset_edges()

    def reset_edges(self):
        self.edges = [list(self.grid[-1,::-1]), list(self.grid[-1::-1,0]), list(self.grid[0,:]), list(self.grid[:,-1])]

    def flipud(self):
        self.grid = np.flipud(self.grid)

    def fliplr(self):
        self.grid = np.fliplr(self.grid)

    def rotate(self, x):
        self.grid = np.rot90(self.grid, x)
        self.neighbors = self.neighbors[-1 * x:] + self.neighbors[:-1 * x]

    def __str__(self):
        return self.id + ': ' + str(self.neighbors) + ', ' + str(self.edges)


def main():
    tiles = {}
    lines = []
    avail = []
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input'), 'r') as file:
        lines = file.read().split('\n\n')
    for line in lines:
        splitLine = line.splitlines()
        tileNum = splitLine.pop(0)[5:-1]
        tiles[tileNum] = Image(tileNum, [list(row) for row in splitLine])
        avail.append(tileNum)

    def findMatch(side, edge):
        nonlocal tiles
        nonlocal avail
        adj = None
        for tile in avail:
            for x in range(4):
                try:
                    idx = tiles[tile].edges.index(edge[::-1])
                    if idx >= 0:
                        rot = (idx + 2 + side) % 4
                        tiles[tile].rotate(rot)
                        # print('found it')
                        adj = tile
                except ValueError:
                    pass
                if x % 2:
                    tiles[tile].flipud()
                else:
                    tiles[tile].fliplr()
                tiles[tile].reset_edges()
        return adj

    for id, tile in list(tiles.items()):
        avail = list(tiles.keys())
        avail.remove(id)
        for idx, neighbor in enumerate(tile.neighbors):
            adj = findMatch(idx, tile.edges[idx])
            tile.neighbors[idx] = adj
    total = 1
    corners = []
    for id, tile in tiles.items():
        print(tile)
        if tile.neighbors.count(None) >= 2:
            corners.append(id)
            total *= int(id)
    print(corners)
    return(total)


if __name__ == "__main__":
    print(main())
