def half_split(arr, char):
    return arr.split(char)[0], arr.split(char)[1]


def is_subset(base_list, subset_list):
    for item in subset_list:
        if item not in base_list:
            return False
    return True


def pt1():
    count = 0
    with open("./day_4_input.txt", "r") as f:
        for line in f:
            first, second = half_split(line, ',')
            first_start, first_end = half_split(first, '-')
            second_start, second_end = half_split(second, '-')

            first_set = list(range(int(first_start), int(first_end)+1))
            second_set = list(range(int(second_start), int(second_end)+1))

            if is_subset(first_set, second_set) or is_subset(second_set, first_set):
                count += 1

    return count


def pt2():
    count = 0
    with open("./day_4_input.txt", "r") as f:
        for line in f:
            first, second = half_split(line, ',')
            first_start, first_end = half_split(first, '-')
            second_start, second_end = half_split(second, '-')

            first_set = range(int(first_start), int(first_end)+1)
            second_set = range(int(second_start), int(second_end)+1)

            for id in first_set:
                if id in second_set:
                    count += 1
                    break

    return count


if __name__ == '__main__':
    print()
    print('--- DAY 4 ---')
    print('1.', pt1())
    print('2.', pt2())
    print()
