import os
import re


def main():
    rules = {}
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input'), 'r') as file:
        lines = file.read().split('\n\n')
        rules = lines[0].splitlines()
        messages = lines[1].splitlines()
        rules = {rule.split(': ')[0]: rule.split(': ')[1] for rule in rules}

    def ruleBuilder(key):
        nonlocal rules
        finalRule = '('
        rule = rules[key].split(' ')
        for ele in rule:
            if ele.isnumeric():
                finalRule += ruleBuilder(ele)
            elif ele == '|':
                finalRule += ele
            else:
                finalRule += ele[1]
        return finalRule + ')'

    oneRule = ruleBuilder('0')
    oneRule = '^' + oneRule + '$'
    reRule = re.compile(oneRule)
    valid = 0
    for message in messages:
        if re.match(reRule, message):
            print(message)
            valid += 1
    return valid





if __name__ == "__main__":
    print(main())
