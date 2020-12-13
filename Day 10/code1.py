import os


def main():
    diffs = {1: 0, 2: 0, 3: 1}
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input'), 'r') as file:
        lines = file.read().splitlines()
        lines = [int(line) for line in lines]
        lines.sort()
        diffs[lines[0]] += 1
        for idx in range(len(lines) - 1):
            diffs[lines[idx + 1] - lines[idx]] += 1
        return diffs[1] * diffs[3]


if __name__ == "__main__":
    print(main())
