import os

dirmap = {
    'nw': (-1, 0),
    'ne': (-1, 1),
    'e': (0, 1),
    'se': (1, 0),
    'sw': (1, -1),
    'w': (0, -1),
}


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
    print(paths)
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
    print(tiles)
    return len(tiles)


if __name__ == "__main__":
    print(main())


# cancel out pairs of se/nw ne/sw