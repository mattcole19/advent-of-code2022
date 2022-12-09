
class Directory:
    def __init__(self, name, parent=None):
        self.name = name
        self.contents = []  # List of files/directories
        self.parent = parent
        self.is_dir = True

    def size(self):
        size = 0
        for content in self.contents:
            if not content.is_dir:
                size += content.size
            else:
                size += content.size()

        return size

    def add_file_to_contents(self, file):
        self.contents.append(file)

    def add_dir_to_contents(self, directory):
        self.contents.append(directory)

    def add_to_contents(self, content):
        if content.startswith('dir'):
            _, name = content.split(' ')
            directory = Directory(name, parent=self)
            self.add_dir_to_contents(directory)
        else:
            size, name = content.split(' ')
            file = File(name, int(size))
            self.add_file_to_contents(file)

    def get_child_dir(self, name):
        for content in self.contents:
            if content.is_dir and content.name == name:
                return content

    def get_all_subdirs(self):
        subdirs = []
        for content in self.contents:
            if content.is_dir:
                subdirs.append(content)
                subdirs.extend(content.get_all_subdirs())
        return subdirs

    def __repr__(self):
        return f'{self.name}'


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.is_dir = False


def part1(file):
    with open(file) as f:
        top_directory = create_dir_structure(f.read().splitlines())

    print(top_directory.size())
    all_dirs = [top_directory] + top_directory.get_all_subdirs()
    print(all_dirs)

    total_size = 0
    for dir_ in all_dirs:
        dir_size = dir_.size()
        print(f'Size of {dir_} is {dir_size}')
        if dir_size < 100000:
            total_size += dir_size
    print(f'Total size is {total_size}')
    return total_size


def create_dir_structure(input_):
    top_directory = Directory('/')
    current_directory = top_directory

    while input_:
        line = input_.pop(0)
        print(line)

        if line == '$ cd /':
            current_directory = top_directory
        elif line.startswith('$ cd'):
            # Change directory here
            target_dir = line.split(' ')[2]
            if target_dir == '..':
                current_directory = current_directory.parent
            else:
                current_directory = current_directory.get_child_dir(target_dir)

        elif line == '$ ls':
            # Go until you hit a $
            while True:
                if input_:
                    line = input_.pop(0)
                    if line.startswith('$'):
                        input_.insert(0, line)
                        break
                    current_directory.add_to_contents(line)
                else:
                    break
        else:
            print(f"FOUND UNEXPECTED LINE: '{line}'")

    return top_directory


def part2(file):
    with open(file) as f:
        top_directory = create_dir_structure(f.read().splitlines())

    total_disk_space = 70000000
    space_needed = 30000000
    unused_space = total_disk_space - top_directory.size()
    goal = space_needed - unused_space
    print(f'Unused space is currently: {unused_space}. We need to free up {goal} space')
    all_dirs = [top_directory] + top_directory.get_all_subdirs()

    smallest_delta = get_dir_with_closest_size(all_dirs, goal, top_directory.size())
    print(f'Smallest delta: {smallest_delta}')
    return smallest_delta


def get_dir_with_closest_size(all_dirs, goal_size, top_dir_size):
    size_to_delete = top_dir_size
    smallest_delta = top_dir_size
    for dir_ in all_dirs:
        dir_size = dir_.size()
        if dir_size < goal_size:
            continue
        delta = dir_size - goal_size
        if delta < smallest_delta:
            smallest_delta = delta
            size_to_delete = dir_size

    return size_to_delete


if __name__ == '__main__':
    # assert part1('test_input.txt') == 95437
    # print(f'The answer to part1 is {part1("input.txt")}')
    assert part2('test_input.txt') == 24933642
    print(f'The answer to part2 is {part2("input.txt")}')
