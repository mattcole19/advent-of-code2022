def part1(file):
    with open(file) as f:
        tree_grid = [[int(char) for char in row if char != '\n'] for row in f.readlines()]

    trees_visible = 0
    top_boundary = 0
    right_boundary = len(tree_grid[0])-1
    left_boundary = 0
    bottom_boundary = len(tree_grid)-1
    for i, row in enumerate(tree_grid):
        for j, tree in enumerate(row):

            # Edges are all visible
            if (i == top_boundary) or (i == bottom_boundary) or (j == left_boundary) or (j == right_boundary):
                trees_visible += 1
                continue

            curr_tree_height = tree_grid[i][j]
            # Check all trees above - until you either find a tree taller (not visible) or hit the edge (visible)

            # If the tree is the tallest in the row, it is visible
            trees_above = above(tree_grid, (i, j))
            trees_right = right(tree_grid, (i, j))
            trees_down = down(tree_grid, (i, j))
            trees_left = left(tree_grid, (i, j))

            trees_to_check = trees_above + trees_right + trees_down + trees_left

            if curr_tree_height > max(trees_above):
                trees_visible += 1
                continue

            if curr_tree_height > max(trees_right):
                trees_visible += 1
                continue

            if curr_tree_height > max(trees_down):
                trees_visible += 1
                continue

            if curr_tree_height > max(trees_left):
                trees_visible += 1
                continue

    for row in tree_grid:
        print(row)
    print(f'Answer: {trees_visible}')
    return trees_visible


def above(grid, curr_tree):
    # Returns all trees above the current tree
    i, j = curr_tree
    result = [row[j] for row in grid[:i]]
    result.reverse()
    return result


def right(grid, curr_tree):
    i, j = curr_tree
    row = grid[i]
    return row[j+1:]


def down(grid, curr_tree):
    i, j = curr_tree

    return [row[j] for row in grid[i+1:]]


def left(grid, curr_tree):
    i, j = curr_tree
    row = grid[i]
    result = row[:j]
    result.reverse()
    return result


def part2(file):

    with open(file) as f:
        tree_grid = [[int(char) for char in row if char != '\n'] for row in f.readlines()]

    highest_scenic_score = 0
    top_boundary = 0
    right_boundary = len(tree_grid[0])-1
    left_boundary = 0
    bottom_boundary = len(tree_grid)-1
    for i, row in enumerate(tree_grid):
        for j, tree in enumerate(row):

            if (i == top_boundary) or (i == bottom_boundary) or (j == left_boundary) or (j == right_boundary):
                continue
            curr_scenic_score = calculate_scenic_score(tree_grid, (i, j))

            if curr_scenic_score > highest_scenic_score:
                highest_scenic_score = curr_scenic_score

            print(f'Tree at {i},{j} has visibility {curr_scenic_score}')

    print(f'Answer: {highest_scenic_score}')
    return highest_scenic_score


def calculate_scenic_score(grid, curr_tree):
    i, j = curr_tree
    curr_tree_height = grid[i][j]
    above_visibility = calculate_visibility(curr_tree_height, above(grid, curr_tree))
    right_visibility = calculate_visibility(curr_tree_height, right(grid, curr_tree))
    down_visibility = calculate_visibility(curr_tree_height, down(grid, curr_tree))
    left_visibility = calculate_visibility(curr_tree_height, left(grid, curr_tree))

    return above_visibility * right_visibility * down_visibility * left_visibility


def calculate_visibility(tree, row):
    visible_trees = 0
    for tree_to_check in row:
        visible_trees += 1
        if tree_to_check >= tree:
            return visible_trees
    return visible_trees


if __name__ == '__main__':
    # assert part1('test_input.txt') == 21
    # print(f'The answer to part1 is {part1("input.txt")}')

    assert part2('test_input.txt') == 8
    print(f'The answer to part2 is {part2("input.txt")}')
