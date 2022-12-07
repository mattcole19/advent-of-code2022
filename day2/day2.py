


def part1():
    with open('input.txt') as file:
        total_score = 0
        for line in file:
            picking_points = 0
            winning_points = 0
            opponent, me = line.split()
            print(f'Opponent chose {opponent}. I chose {me}')

            if me == 'X':  # ROCK
                picking_points += 1

                if opponent == 'A':
                    winning_points += 3
                elif opponent == 'C':
                    winning_points += 6
            elif me == 'Y': # PAPER
                picking_points += 2

                if opponent == 'A':
                    winning_points += 6
                elif opponent == 'B':
                    winning_points += 3
            else: # SCISSORS
                picking_points += 3

                if opponent == 'B':
                    winning_points += 6
                elif opponent == 'C':
                    winning_points += 3
            round_score = picking_points + winning_points
            total_score += round_score
        print(total_score)

    return total_score

def part2():
    # X = lose. Y = draw. Z = win
    with open('input.txt') as file:
        rock = 1
        paper = 2
        scissors = 3
        total_score = 0
        for line in file:
            opponent, outcome = line.split()

            if opponent == 'A':
                if outcome == 'X':
                    choice = scissors
                elif outcome == 'Y':
                    choice = rock
                else:
                    choice = paper

            elif opponent == 'B':
                if outcome == 'X':
                    choice = rock
                elif outcome == 'Y':
                    choice = paper
                else:
                    choice = scissors

            elif opponent == 'C':
                if outcome == 'X':
                    choice = paper
                elif outcome == 'Y':
                    choice = scissors
                else:
                    choice = rock

            # Def right
            match outcome:
                case 'X':
                    winning_points = 0
                case 'Y':
                    winning_points = 3
                case 'Z':
                    winning_points = 6

            # Def right
            round_score = choice + winning_points
            total_score += round_score
        print(total_score)
    return total_score


if __name__ == "__main__":
    part2()
