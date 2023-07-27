def pt1(lines):
    # (axis [0 = y, 1 = x], value +-)
    moves = {
        'U': (1, 1),
        'D': (1, -1),
        'L': (0, -1),
        'R': (0, 1)
    }

    head = [0, 0]
    tail = [0, 0]

    pos = set()
    pos.add((0, 0))

    index = 0
    for line in lines:
        index += 1
        d, amount = line.split(' ')[0], int(line.split(' ')[1])

        for _ in range(amount):
            axis = moves[d][0]
            value = moves[d][1]

            head[axis] += value
            
            # negative = left :: positive = right :: zero = same column
            x_diff = head[0] - tail[0]     

            # negative = below :: positive = above :: zero = same row
            y_diff = head[1] - tail[1]       

            if abs(x_diff) == 2:
                tail[0] += int(x_diff / 2)

                if y_diff != 0:
                    tail[1] += y_diff
            
            if abs(y_diff) == 2:
                tail[1] += int(y_diff / 2)

                if x_diff != 0:
                    tail[0] += x_diff            


            new_pos = (tail[0], tail[1])
            pos.add(new_pos)

    return len(pos)

def pt2(lines):
    pass

if __name__ == '__main__':
    DAY = 9

    lines = []
    with open(f"./day_{DAY}_input.txt", "r") as f:
        lines = [line for line in f]

    print()
    print(f'--- DAY {DAY} ---')
    print('1.', pt1(lines))
    print('2.', pt2(lines))
    print()
