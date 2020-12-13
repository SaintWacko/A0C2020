import os
import sys
import math


def main():
    lines = []
    bestBus = None
    minWait = sys.maxsize
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input'), 'r') as file:
        lines = file.read().splitlines()
    time = int(lines[0])
    buses = [int(bus) for bus in lines[1].split(',') if bus != 'x']
    for bus in buses:
        wait = math.ceil(time / bus) * bus - time
        if wait < minWait:
            bestBus = bus
            minWait = wait
    return bestBus * minWait


if __name__ == "__main__":
    print(main())
