def main():
    with open('input', 'r') as file:
        tAnswers = 0
        lines = file.read().split('\n\n')
        for group in lines:
            members = group.split('\n')
            temp = list(members.pop())
            for member in members:
                temp = list(set(temp) & set(member))
            tAnswers += len(temp)
        return tAnswers


if __name__ == "__main__":
    print(main())
