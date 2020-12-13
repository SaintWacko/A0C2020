import os


def main():
    invalid = 41682220
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input'), 'r') as file:
        lines = file.read().splitlines()
        lines = [int(line) for line in lines]
        for idx in range(len(lines)):
            sum = lines[idx]
            sumRange = []
            for line in lines[idx + 1:]:
                sum += line
                sumRange.append(line)
                if sum > invalid:
                    break
                if sum == invalid:
                    sumRange.sort()
                    return sumRange[0] + sumRange[-1]



if __name__ == "__main__":
    print(main())
