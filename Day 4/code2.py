import re
REQUIRED_KEYS = {
    'byr': lambda x: 1920 <= int(x) <= 2002,
    'iyr': lambda x: 2010 <= int(x) <= 2020,
    'eyr': lambda x: 2020 <= int(x) <= 2030,
    'hgt': lambda x: validate_height(x),
    'hcl': lambda x: re.compile(r'^#[0-9a-f]{6}$').match(x),
    'ecl': lambda x: x in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'),
    'pid': lambda x: re.compile(r'^[0-9]{9}$').match(x),
}


def validate_height(x):
    unit = x[-2:]
    num = int(x[:-2])
    if unit == 'in':
        return 59 <= num <= 76
    if unit == 'cm':
        return 150 <= num <= 193
    return False


def main():
    with open('input', 'r') as file:
        lines = file.read().split('\n\n')
        valid_lines = 0
        for line in lines:
            parsedLine = line.replace('\n', ' ')
            lineDict = {k: v for (k, v) in [pair.split(':') for pair in parsedLine.split(' ')]}
            missingKeys = set(REQUIRED_KEYS) - set(lineDict)
            if not len(missingKeys):
                valid = True
                for key in REQUIRED_KEYS:
                    if not REQUIRED_KEYS[key](lineDict[key]):
                        valid = False
                        break
                if valid:
                    valid_lines += 1

    return valid_lines


if __name__ == "__main__":
    print(main())
