def pt1(lines):
    pass


def pt2(lines):
    pass


if __name__ == '__main__':
    DAY = 0

    lines = []
    with open(f"./day_{DAY}_input.txt", "r") as f:
        lines = [line for line in f]

    print()
    print(f'--- DAY {DAY} ---')
    print('1.', pt1(lines))
    print('2.', pt2(lines))
    print()
