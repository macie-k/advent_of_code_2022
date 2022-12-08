class File:
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size
        

class Directory:
    def __init__(self, name: str, parent_dir):
        self.name = name
        self.parent_dir = parent_dir if parent_dir is not None else self
        self.children = set()

    def add_child(self, child):
        self.children.add(child)

    def get_total_size(self):
        size = 0
        for child in self.children:
            if type(child) is Directory:
                size += child.get_total_size()
            
            if type(child) is File:
                size += child.size
        return size


def pt1(lines):
    dir_list: list[Directory] = []
    current_dir = None
    
    for line in lines:
        words = line.split()

        # changing directory
        if words[1] == 'cd':
            if words[2] == '..':
                current_dir = current_dir.parent_dir
                continue

            # check if destination directory already exists
            new_dir = None
            for dir in dir_list:
                if dir.name == words[2] and dir.parent_dir == current_dir:
                    new_dir = dir
                    break

            # if destination doesn't exist create it
            if new_dir is None:
                new_dir = Directory(words[2], current_dir if words[2] != '/' else None)                    
                dir_list.append(new_dir)

            current_dir = new_dir
        
        # directory listing
        if words[0] == 'dir':

            # check if directory already added
            added = False
            for dir in dir_list:
                if dir.name == words[1] and dir.parent_dir == current_dir:
                    added = True

            if added: continue

            # create and add if not
            dir_list.append(Directory(words[1], current_dir))
            current_dir.add_child(dir_list[-1])
        
        # add file as current directory child
        if words[0].isnumeric():
            current_dir.add_child(File(words[1], int(words[0])))

    result = 0
    for dir in dir_list:
        total = dir.get_total_size()
        if total < 100_000:
            result += total
    
    return result, dir_list


def pt2(dir_list: list[Directory]):
    TOTAL_SIZE = 70_000_000
    REQUIRED_SIZE = 30_000_000
    HOME_SIZE = dir_list[0].get_total_size()
    MIN_TO_FREE = REQUIRED_SIZE - (TOTAL_SIZE - HOME_SIZE)

    min_enough = float("inf")
    for dir in dir_list:
        total = dir.get_total_size()
        if total >= MIN_TO_FREE and total < min_enough:
            min_enough = total

    return min_enough


if __name__ == '__main__':
    lines = []
    with open("./day_7_input.txt", "r") as f:
        lines = [line for line in f]

    pt1_result, dir_list = pt1(lines)

    print()
    print('--- DAY 7 ---')
    print('1.', pt1_result)
    print('2.', pt2(dir_list))
    print()


