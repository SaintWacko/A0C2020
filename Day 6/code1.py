def main():
    with open('input', 'r') as file:
        tAnswers = 0
        lines = file.read().split('\n\n')
        for line in lines:
            answers = set(line.replace('\n', ''))
            tAnswers += len(answers)
        return tAnswers


if __name__ == "__main__":
    print(main())
