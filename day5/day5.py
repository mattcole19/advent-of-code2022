from collections import namedtuple

Direction = namedtuple('Direction', 'num start end')


def part1(file):
    answer = 0
    with open(file) as f:
        stacks, directions = parse_input(f.read())

        for direction in directions:
            execute_direction(direction, stacks)

    print(f'Ending stacks:')
    for stack in stacks:
        print(stack)

    answer = ''.join([stack.pop()[1] for stack in stacks])
    print(f'Answer: {answer}')

    return answer


def part2(file):
    with open(file) as f:
        stacks, directions = parse_input(f.read())
        for direction in directions:
            execute_direction2(direction, stacks)
    answer = ''.join([stack.pop()[1] for stack in stacks])
    print(f'Answer: {answer}')
    return answer


def parse_input(input_string: str):
    # Split the input into two parts: the initial stack state and the directions.
    stacks_input, directions_input = input_string.split('\n\n')
    # print(f'Part1: \n{part1}')
    # print('----------------')
    # print(f'Part2: \n{part2}')
    stacks = parse_stacks(stacks_input)
    directions = parse_directions(directions_input)

    return stacks, directions


def parse_stacks(stacks_input: str):
    # Parse part1 of the input into stacks
    # Start by getting the columns...
    # Every element takes up 3 characters, then there is a space to seperate
    lines = stacks_input.splitlines()
    lines.reverse()
    # reader = csv.reader(lines, delimiter=' ')
    # for row in reader:
    #     print(row)
    # # Get number of stacks
    top_line = lines[0]
    num_stacks = int(top_line[-1])
    # print(f'Num stacks: {num_stacks}')
    # print(top_line)

    # Stack1 would be [line1[0:3], line2[0, 3] ... linen[0, 3]]
    # Stack2 would be [line1[4:7], line2[4:7]... linen[4:7]]
    # Stack3 would be [line1[8:11], line2[8:11]... linen[8:11]]
    # ...
    # StackN would be [line1[(n-1)*4:(n-1)*4+3], line2[prev_end: start+3]... linen[prev_end: start+3]
    stack1 = []
    stack2 = []
    for line in lines[1:]:
        print(f'{line}')
        element = line[0:3]
        if element.strip():
            stack1.append(element)

        element = line[4:7]
        if element.strip():
            stack2.append(element)
    stacks = []
    for n in range(num_stacks):
        start = n*4
        end = start + 3
        stack = [line[start:end] for line in lines[1:] if line[start:end].strip()]
        stacks.append(stack)

    for stack in stacks:
        print(stack)

    return stacks


def parse_directions(directions_input: str):
    directions = []
    for direction_str in directions_input.splitlines():
        direction_str_split = direction_str.split(' ')
        direction = Direction(int(direction_str_split[1]), int(direction_str_split[3]), int(direction_str_split[5]))
        directions.append(direction)
        print(direction)
    return directions


def execute_direction(direction: Direction, stacks: list):
    print(f'Moving {direction.num} from {direction.start} to {direction.end}')

    for _ in range(direction.num):
        stacks[direction.end-1].append(stacks[direction.start-1].pop())


def execute_direction2(direction: Direction, stacks: list):
    lst = []
    for _ in range(direction.num):
        lst.insert(0, stacks[direction.start-1].pop())

    stacks[direction.end-1].extend(lst)


if __name__ == '__main__':
    # assert part1('test_input.txt') == "CMZ"
    # print(f'Answer to part1: {part1("input.txt")}')
    assert part2('test_input.txt') == "MCD"
    print(f'Answer to part2: {part2("input.txt")}')

