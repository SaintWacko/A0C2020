import os
import re
ruleParse = re.compile(r'(?P<name>[\w ]+): (?P<min1>\d+)-(?P<max1>\d+) or (?P<min2>\d+)-(?P<max2>\d+)')


def main():
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input'), 'r') as file:
        lines = file.read().split('\n\n')
        rules = lines[0].splitlines()
        tickets = lines[2].splitlines()[1:]
        tickets = [[int(val) for val in ticket.split(',')] for ticket in tickets]
        valid = set()
        invalid = 0
        for rule in rules:
            match = ruleParse.match(rule)
            min1 = int(match.group('min1'))
            max1 = int(match.group('max1'))
            for i in range(min1, max1 + 1):
                valid.add(i)
            min2 = int(match.group('min2'))
            max2 = int(match.group('max2'))
            for i in range(min2, max2 + 1):
                valid.add(i)
        for ticket in tickets:
            for value in ticket:
                if value not in valid:
                    invalid += value
        return invalid


if __name__ == "__main__":
    print(main())
