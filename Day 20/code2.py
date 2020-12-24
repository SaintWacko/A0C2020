import os
import math
import numpy as np


class Image():
    # [B, L, T, R]

    def __init__(self, id, image):
        self.id = int(id)
        self.edges = []
        self.neighbors = [None, None, None, None]
        self.grid = np.array(image)
        self.reset_edges()
        self.flipv = 0
        self.fliph = 0

    def reset_edges(self):
        self.edges = [list(self.grid[-1, ::-1]), list(self.grid[-1::-1, 0]), list(self.grid[0, :]), list(self.grid[:, -1])]

    def flipud(self):
        # print('flipv ', self.id)
        self.flipv += 1
        self.grid = np.flipud(self.grid)
        self.neighbors[0], self.neighbors[2] = self.neighbors[2], self.neighbors[0]
        self.reset_edges()

    def fliplr(self):
        # print('fliph ', self.id)
        self.fliph += 1
        self.grid = np.fliplr(self.grid)
        self.neighbors[1], self.neighbors[3] = self.neighbors[3], self.neighbors[1]
        self.reset_edges()

    def rotate(self, x):
        # print('rot', x, self.id)
        self.grid = np.rot90(self.grid, x)
        self.neighbors = self.neighbors[-1 * x:] + self.neighbors[:-1 * x]
        self.reset_edges()

    def __str__(self):
        return str(self.id) + ': ' + str(self.neighbors) + ', ' + str(self.edges) + ' v: ' + str(self.flipv) + ' h: ' + str(self.fliph)


def main():
    tiles = {}
    lines = []
    avail = []
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input'), 'r') as file:
        lines = file.read().split('\n\n')
    size = int(math.sqrt(len(lines)))
    for line in lines:
        splitLine = line.splitlines()
        tileNum = splitLine.pop(0)[5:-1]
        tiles[int(tileNum)] = Image(tileNum, [[int(ch) for ch in list(row.replace('.', '0').replace('#', '1'))] for row in splitLine])
        avail.append(int(tileNum))

    def findMatch(side, edge):
        nonlocal tiles
        nonlocal avail
        for tile in tiles.keys():
            for x in range(2):
                try:
                    idx = tiles[tile].edges.index(edge[::-1])
                    if idx >= 0:
                        rot = (idx + 2 - side) % 4
                        tiles[tile].rotate(rot)
                        return tile
                except ValueError:
                    pass
                if tile in avail:
                    tiles[tile].flipud()
        return None

    toCheck = [avail[0]]
    index = 0
    while index < len(toCheck):
        tile = tiles[toCheck[index]]
        avail.remove(tile.id)
        for idx, neighbor in enumerate(tile.neighbors):
            adj = findMatch(idx, tile.edges[idx])
            tile.neighbors[idx] = adj
            if adj:
                if adj not in toCheck:
                    toCheck.append(adj)
        index += 1

    grid = np.zeros((size, size))
    for id, tile in list(tiles.items()):
        print(tile)
        if not tile.neighbors[1] and not tile.neighbors[2]:
            grid[0][0] = id
    for (idy, idx), id in np.ndenumerate(grid):
        tile = tiles[id]
        if tile.neighbors[0]:
            grid[idy + 1][idx] = tile.neighbors[0]
        if tile.neighbors[3]:
            grid[idy][idx + 1] = tile.neighbors[3]
    print(grid)
    image = np.concatenate([np.concatenate([tiles[id].grid[1:-1, 1:-1] for id in row], axis=1) for row in grid], axis=0)

    monster = [
        '00000000000000000010',
        '10000110000110000111',
        '01001001001001001000'
    ]
    monster = np.array([[int(bit) for bit in row] for row in monster])
    print(monster)

    def isMonster(slice):
        nonlocal monster
        for (idy, idx), bit in np.ndenumerate(slice):
            if monster[idy][idx]:
                if not bit:
                    return False
        return True
        
    monsters = 0
    print(image)
    for _ in range(2):
        for _ in range(4):
            for (idy, idx), bit in np.ndenumerate(image[:-2, :-19]):
                if idy == 2 and idx == 2:
                    print(image[idy:idy + 3, idx:idx + 20])
                if isMonster(image[idy:idy + 3, idx:idx + 20]):
                    monsters += 1
            if monsters:
                break
            image = np.rot90(image)
        image = np.fliplr(image)
    return sum(image.flatten()) - sum(monster.flatten()) * monsters


if __name__ == "__main__":
    print(main())
