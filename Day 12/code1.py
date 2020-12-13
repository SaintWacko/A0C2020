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
    positionY = 0
    positionX = 0
    currentHeading = 1

    def move(direction, distance):
        nonlocal positionX
        nonlocal positionY
        if direction in directionY:
            positionY += distance * directionY[direction]
        elif direction in directionX:
            positionX += distance * directionX[direction]

    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input'), 'r') as file:
        lines = file.read().splitlines()
    for line in lines:
        if line[0] in directions:
            move(line[0], int(line[1:]))
        elif line[0] == 'F':
            move(directions[currentHeading], int(line[1:]))
        else:
            currentHeading = int(currentHeading + (1 if line[0] == 'R' else -1) * (int(line[1:]) / 90)) % 4
    return abs(positionX) + abs(positionY)


if __name__ == "__main__":
    print(main())
