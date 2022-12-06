def find_n_distinct(data, n):
    result = n
    buffer = [*data[slice(n)]]  # unpack string to an array of n chars

    buffer_set = set(buffer)
    if len(buffer_set) == len(buffer):
        return result

    for char in data[n:]:
        result += 1
        buffer.pop(0)
        buffer.append(char)

        buffer_set = set(buffer)    # create set to remove duplicates
        if len(buffer_set) == len(buffer):
            break

    return result


def pt1(lines):
    return find_n_distinct(lines[0], 4)


def pt2(lines):
    return find_n_distinct(lines[0], 14)


if __name__ == '__main__':
    lines = []
    with open("./day_6_input.txt", "r") as f:
        lines = [line for line in f]

    print()
    print('--- DAY 6 ---')
    print('1.', pt1(lines))
    print('2.', pt2(lines))
    print()
