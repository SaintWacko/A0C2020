def main():
    with open('input', 'r') as file:
        lines = file.read().splitlines()
        dx = 3
        dy = 1
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
        return trees


if __name__ == "__main__":
    print(main())
