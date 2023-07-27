def pt1(lines):
    X = 1
    X_QUEUE = None   # {val: number, target_cycle: number}
    SUM = 0

    cycle = 0
    index = 0
    while True:
        if index == len(lines):
            break

        line = lines[index]
        instr = line.split(' ')[0]
        cycle += 1

        if instr == 'noop':
            index += 1

        if instr == 'addx' and X_QUEUE is None:
            X_QUEUE = {'val': int(line.split(' ')[1]), 'target_cycle': cycle + 1}

        # signal count
        if (cycle - 20) % 40 == 0:
            SUM += X * cycle

        # removing from queue
        if X_QUEUE is not None and X_QUEUE['target_cycle'] == cycle:
            X += X_QUEUE['val']
            X_QUEUE = None
            index += 1

    return SUM


def pt2(lines):
    pass


if __name__ == '__main__':
    DAY = 10

    lines = []
    with open(f"./day_{DAY}_input.txt", "r") as f:
        lines = [line.replace('\n', '') for line in f]

    print()
    print(f'--- DAY {DAY} ---')
    print('1.', pt1(lines))
    print('2.', pt2(lines))
    print()
