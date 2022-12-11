def is_visible(grid, current, loop_range, i = None, j = None):
    for x in loop_range:
        if grid[x if i is None else i][x if j is None else j] >= current:
            return False

    return True


def get_score(grid, current, loop_range, i = None, j = None):
    score = 0
    for x in loop_range:
        tree = grid[x if i is None else i][x if j is None else j]
        score += 1

        if tree >= current:
            break

    return score


def pt1(lines):
    grid = []

    for line in lines:
        grid.append(list(line.rstrip()))
    
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):

            # if tree is on edge
            if i in [0, len(grid) - 1] or j in [0, len(grid[i]) - 1]: 
                count += 1
                continue

            current = grid[i][j]

            if is_visible(grid, current, range(i), j=j) \
            or is_visible(grid, current, range(i+1, len(grid)), j=j) \
            or is_visible(grid, current, range(j), i=i) \
            or is_visible(grid, current, range(j+1, len(grid[i])), i=i):
                count += 1 
            
    return count


def pt2(lines):
    grid = []

    for line in lines:
        grid.append(list(line.rstrip()))
    
    max_score = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            current = grid[i][j]

            score = get_score(grid, current, range(i-1, -1, -1), j=j)
            score *= get_score(grid, current, range(i+1, len(grid)), j=j)
            score *= get_score(grid, current, range(j-1, -1, -1), i=i)
            score *= get_score(grid, current, range(j+1, len(grid[i])), i=i)

            if score > max_score:
                max_score = score

    return max_score


if __name__ == '__main__':
    lines = []
    with open("./day_8_input.txt", "r") as f:
        lines = [line for line in f]
    
    print()
    print('--- DAY 8 ---')
    print('1.', pt1(lines))
    print('2.', pt2(lines))
    print()
