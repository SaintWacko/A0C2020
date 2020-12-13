import os


def main():
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input'), 'r') as file:
        lines = file.read().splitlines()
        for idx in range(26, len(lines)):
            preamble = [int(line) for line in lines[idx - 25:idx]]
            preamble.sort()
            print(preamble)
            current = int(lines[idx])
            valid = False
            for pidx in range(25):
                for num in preamble[pidx:]:
                    sum = preamble[pidx] + num
                    print(sum, '==', current)
                    if sum > current:
                        break
                    if sum == current:
                        valid = True
                if valid:
                    break
            if not valid:
                return current


if __name__ == "__main__":
    print(main())
