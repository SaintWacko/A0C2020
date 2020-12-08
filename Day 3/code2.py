def main():
    slopes = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2),
    ]
    with open('input', 'r') as file:
        lines = file.read().splitlines()
        totalTrees = 1
        for slope in slopes:
            dx, dy = slope
            x = dx
            y = dy
            trees = 0
            while y < len(lines):
                if lines[y][x] == '#':
                    trees += 1
                x += dx
                if x >= len(lines[y]):
                    x -= len(lines[y])
                y += dy
            totalTrees *= trees
        return totalTrees


if __name__ == "__main__":
    print(main())
