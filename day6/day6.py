
def part1(file):
    with open(file) as f:
        string = f.read()
        for i in range(0, len(string)-4):
            print(f'Checking {string[i:i+4]}')
            if not has_duplicates(string[i:i+4]):
                return i + 4
    return -1


def part2(file):
    with open(file) as f:
        string = f.read()
        for i in range(0, len(string)-14):
            print(f'Checking {string[i:i+14]}')
            if not has_duplicates(string[i:i+14]):
                return i + 14
    return -1


def has_duplicates(string):
    letters_seen = set()
    for letter in string:
        if letter in letters_seen:
            return True
        letters_seen.add(letter)
    return False


if __name__ == '__main__':
    # assert part1('test_input.txt') == 5
    print(f'The answer to part1 is {part1("input.txt")}')
    assert part2('test_input.txt') == 19
    print(f'The answer to part2 is {part2("input.txt")}')

