KEY_START, KEY_END = 'start', 'end'


def create_object(letter):
    return {
        KEY_START: letter,
        KEY_END: letter
    }


def main():
    string = input().replace(' ', '')
    letter_set = sorted(set(list(string)))

    if not letter_set:
        print()
        return

    ranges = []
    current_range = create_object(letter_set[0])

    for i in range(1, len(letter_set)):
        letter = letter_set[i]
        if ord(current_range[KEY_END]) + 1 == ord(letter):
            current_range[KEY_END] = letter
        else:
            ranges.append(current_range)
            current_range = create_object(letter)
    ranges.append(current_range)

    ranges = ['{}:{}'.format(data[KEY_START], data[KEY_END]) for data in ranges]
    print(', '.join(ranges))


if __name__ == '__main__':
    while True:
        try:
            main()
        except EOFError:
            break
