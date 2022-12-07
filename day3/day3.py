def part1():
    answer = 0
    with open('input.txt') as file:
        for line in file:
            first, second = split_sack(line)
            print(f'First: {first}. Second: {second}')
            found = False
            for letter in first:
                if letter in second:
                    print(f'Letter {letter} found!')
                    answer += letter_to_priority(letter)
                    break


    print(f'The answer for part 1 is {answer}')


def part2(input):
    answer = 0

    # Split input into groups of 3
    groups = []
    with open(input) as file:
        group = []
        for line in file:
            group.append(line.strip())
            if len(group) == 3:
                # Create new group
                groups.append(group.copy())
                group = []
        print(groups)

        for group in groups:
            badge = find_similar_item(group)
            answer += letter_to_priority(badge)


    print(f'The answer for part 2 is {answer}')

    return answer


def letter_to_priority(letter: str) -> int:
    if letter.islower():
        return ord(letter) - 96
    return ord(letter) - 38


def split_sack(string):
    return string[:len(string)//2], string[len(string)//2:]


def find_similar_item(group: list) -> str:
    first, second, third = group
    for letter in first:
        if (letter in second) and (letter in third):
            return letter


if __name__ == '__main__':
    #print(split_sack('vJrwpWtwJgWrhcsFMMfFFhFp'))
    print(letter_to_priority('z'))
    # part1()
    assert part2('test_input.txt') == 70
    part2('input.txt')
