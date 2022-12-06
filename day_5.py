def load_stacks():
    stacks = {}
    with open("./day_5_input.txt", "r") as f:
        for line in f:
            if '1' in line: break

            col_num = 1
            for index in range(1, len(line), 4):
                if line[index] != ' ':
                    if stacks.get(col_num) is None:
                        stacks[col_num] = []
                    stacks[col_num].insert(0, line[index])
                col_num += 1
                        
    return stacks


def pt1():
    stacks = load_stacks()

    with open("./day_5_input.txt", "r") as f:
        for line in f:
            if 'move' not in line: continue

            word_split = line.split()

            amount = int(word_split[1])
            from_i = int(word_split[3])
            to_i = int(word_split[5])

            for _ in range(amount):
                stacks[to_i].append(stacks[from_i].pop())
    
    stacks_str = ''
    for i in range(len(stacks)):
        stacks_str += stacks[i+1][-1]

    return stacks_str


def pt2():
    stacks = load_stacks()

    with open("./day_5_input.txt", "r") as f:
        for line in f:
            if 'move' not in line: continue

            word_split = line.split()

            amount = int(word_split[1])
            from_i = int(word_split[3])
            to_i = int(word_split[5])

            start_index = len(stacks[to_i])
            for _ in range(amount):
                stacks[to_i].insert(start_index, stacks[from_i].pop())
    
    stacks_str = ''
    for i in range(len(stacks)):
        stacks_str += stacks[i+1][-1]

    return stacks_str


if __name__ == '__main__':
    print()
    print('--- DAY 5 ---')
    print('1.', pt1())
    print('2.', pt2())
    print()
