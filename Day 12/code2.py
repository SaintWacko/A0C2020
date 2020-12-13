import os


directionY = {
    'N': 1,
    'S': -1,
}
directionX = {
    'E': 1,
    'W': -1,
}
directions = ['N', 'E', 'S', 'W']


def main():
    wpY = 1
    wpX = 10
    shipY = 0
    shipX = 0

    def move(direction, distance):
        nonlocal wpX
        nonlocal wpY
        if direction in directionY:
            wpY += distance * directionY[direction]
        elif direction in directionX:
            wpX += distance * directionX[direction]

    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input'), 'r') as file:
        lines = file.read().splitlines()
    for line in lines:
        if line[0] in directions:
            move(line[0], int(line[1:]))
        elif line[0] == 'F':
            rpt = int(line[1:])
            while rpt:
                shipY += wpY
                shipX += wpX
                rpt -= 1
        else:
            rpt = int(line[1:]) / 90
            while rpt:
                if line[0] == 'L':
                    wpX, wpY = wpY * -1, wpX
                if line[0] == 'R':
                    wpX, wpY = wpY, wpX * -1
                rpt -= 1
    return abs(shipX) + abs(shipY)


if __name__ == "__main__":
    print(main())
