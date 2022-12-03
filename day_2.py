# A - rock
# B - paper
# C - scissors
# X - rock - 1
# Y - paper - 2
# Z - scissors - 3

def pt1():
    matches = {
        'A X': 4,
        'A Y': 8,
        'A Z': 3,
        'B X': 1,
        'B Y': 5,
        'B Z': 9,
        'C X': 7,
        'C Y': 2,
        'C Z': 6,
    }

    result = 0
    with open("./day_2_input.txt", "r") as f:
        for line in f:
            result += matches[line.strip()]

    return result

# A - rock - 1
# B - paper - 2
# C - scissors - 3
# X - lose
# Y - draw
# Z - win


def pt2():
    matches = {
        'A X': 3,
        'A Y': 4,
        'A Z': 8,
        'B X': 1,
        'B Y': 5,
        'B Z': 9,
        'C X': 2,
        'C Y': 6,
        'C Z': 7,
    }

    result = 0
    with open("./day_2_input.txt", "r") as f:
        for line in f:
            result += matches[line.strip()]

    return result


if __name__ == '__main__':
    print()
    print('--- DAY 2 ---')
    print('1.', pt1())
    print('2.', pt2())
    print()
