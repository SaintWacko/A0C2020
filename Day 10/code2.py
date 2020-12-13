import os


def memoize(f):
    memo = {}

    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]
    return helper


def main():
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input'), 'r') as file:
        lines = file.read().splitlines()
        lines = [int(line) for line in lines]
        lines.sort()
        lines.insert(0, 0)

        def counter(index):
            if index == len(lines) - 1:
                return 1
            count = 0
            for idx in range(index + 1, len(lines)):
                if lines[idx] <= lines[index] + 3:
                    count += counter(idx)
            return count

        counter = memoize(counter)
        return counter(0)







if __name__ == "__main__":
    print(main())
