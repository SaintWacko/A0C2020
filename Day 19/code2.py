import os
import re


def main():
    rules = {}
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input'), 'r') as file:
        lines = file.read().split('\n\n')
        rules = lines[0].splitlines()
        messages = lines[1].splitlines()
        rules = {rule.split(': ')[0]: rule.split(': ')[1] for rule in rules}
        rules['8'] = '42 | 42 8'
        rules['11'] = '42 31 | 42 11 31'

    def ruleBuilder(key, level=0):
        if level > 13:
            return ''
        nonlocal rules
        finalRule = '('
        rule = rules[key].split(' ')
        for ele in rule:
            if ele.isnumeric():
                finalRule += ruleBuilder(ele, level + 1)
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

# import os
# import re


# def main():
#     rules = {}
#     with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input'), 'r') as file:
#         lines = file.read().split('\n\n')
#         rules = lines[0].splitlines()
#         messages = lines[1].splitlines()
#         rules = {rule.split(': ')[0]: rule.split(': ')[1] for rule in rules}
#         rules['8'] = '42 | 42 8'
#         rules['11'] = '42 31 | 42 11 31'

#     def ruleBuilder(key):
#         nonlocal rules
#         finalRule = '('
#         rule = rules[key].split(' ')
#         for ele in rule:
#             if ele.isnumeric():
#                 if ele == key:
#                     finalRule += '(?P<r' + key + '>.*)'
#                 else:
#                     finalRule += ruleBuilder(ele)
#             elif ele == '|':
#                 finalRule += ele
#             else:
#                 finalRule += ele[1]
#         return finalRule + ')'
    
#     def checkLoop(match):
#         groups = match.groupdict()
#         # print(groups)
#         if not any(groups.values()):
#             return 1
#         for key, value in groups.items():
#             if value:
#                 print(key, ': ', value)
#                 subRule = ruleBuilder(key[1:])
#                 subRule = '^' + subRule + '$'
#                 print(subRule)
#                 subMatch = re.match(subRule, value)
#                 if subMatch:
#                     return checkLoop(subMatch)
#         return 0

#     oneRule = ruleBuilder('0')
#     oneRule = '^' + oneRule + '$'
#     print(oneRule)
#     reRule = re.compile(oneRule)
#     valid = 0
#     for message in messages:
#         match = re.match(reRule, message)
#         if match:
#             temp = checkLoop(match)
#             # print(temp, ': ', message)
#             valid += temp
#         else:
#             print('0 : ', message)

#     return valid





# if __name__ == "__main__":
#     print(main())
