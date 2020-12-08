
def main():
    with open('input', 'r') as file:
        lines = file.read().splitlines()
        lines = [int(x) for x in lines]
        lines.sort()
        for idx in range(len(lines) - 1):
            idx2 = idx + 1
            while idx2 < len(lines):
                sum = int(lines[idx]) + int(lines[idx2])
                # print(sum)
                if sum == 2020:
                    return lines[idx] * lines[idx2]
                elif sum > 2020:
                    break
                else:
                    idx2 += 1


if __name__ == "__main__":
    print(main())
