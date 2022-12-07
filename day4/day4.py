def part1(file):
    answer = 0
    with open(file) as f:
        for line in f:
            pair1, pair2 = get_pairs(line)
            large_range, small_range = order_pairs(pair1, pair2)
            print(f'Large: {large_range}, Small: {small_range}')

            if (small_range[0] in large_range) and (small_range[-1] in large_range):
                answer += 1
    return answer



def part2(file):
    answer = 0
    with open(file) as f:
        for line in f:
            pair1, pair2 = get_pairs(line)
            pair1, pair2 = order_pairs2(pair1, pair2)

            for num in pair1:
                if num in pair2:
                    answer += 1
                    break

    return answer


def get_pairs(line):
    pair1, pair2 = line.split(',')
    pair1_nums = pair1.split('-')
    pair1_range = range(int(pair1_nums[0]), int(pair1_nums[1]) + 1)
    pair2_nums = pair2.split('-')
    pair2_range = range(int(pair2_nums[0]), int(pair2_nums[1]) + 1)

    return pair1_range, pair2_range


def order_pairs(pair1, pair2):
    # Returns the pair with a larger range first
    if len(pair1) >= len(pair2):
        return pair1, pair2
    return pair2, pair1


def order_pairs2(pair1, pair2):
    # Returns the pair with lowest start first
    if pair1[0] <= pair2[0]:
        return pair1, pair2
    return pair2, pair1




def playground():
    print(len(range(5)))
    #assert range(2, 3) in range(5)



if __name__ == '__main__':
    # playground()
    # assert part1('test_input.txt') == 2
    # print(f'Part1 answer: {part1("input.txt")}')
    assert part2('test_input.txt') == 4
    print(f'Part2 answer: {part2("input.txt")}')