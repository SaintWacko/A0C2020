import re
PATTERN = re.compile(r'(?P<min>\d+)-(?P<max>\d+) (?P<rule>[a-z]): (?P<pw>.+)')


def main():
    with open('input', 'r') as file:
        lines = file.read().splitlines()
        valid = 0
        for line in lines:
            match = PATTERN.match(line)
            min = int(match.group('min'))
            max = int(match.group('max'))
            rule = match.group('rule')
            pw = match.group('pw')
            count = pw.count(rule)
            if count <= max and count >= min:
                valid += 1
    return valid


if __name__ == "__main__":
    print(main())
