def part1(file):
    start = [0, 0] # x, y
    unique_positions_visited = set(start)
    head = start
    with open(file) as f:
        for line in f:
            print(f'Head at {head}')
            direction, steps = line.split()
            print(f'Direction: {direction}, steps: {steps}')

            # Move the head
            match direction:
                case "U":
                    head[1] += 1
                case "R":
                    head[0] += 1
                case "D":
                    head[1] -= 1
                case "L":
                    head[0] -= 1



    return


def part2(file):
    return


if __name__ == '__main__':
    pass
    # part1('input.txt')
    # part2('input.txt')
