# a-z == 1-26 :: a-z === 97-122
# diff = 96

# A-Z == 27-52 :: A-Z === 65-90
# diff = 38

def pt1():
    repeats = []
    with open("./day_3_input.txt", "r") as f:
        for line in f:
            half_len = int(len(line) / 2)
            half = line[slice(0, half_len)]
            rest = line[slice(half_len, half_len*2)]

            for letter in rest:
                if letter in half:
                    ascii = ord(letter)
                    repeats.append(ascii - 96 if ascii >= 97 else ascii - 38)
                    break

    return sum(repeats)


def pt2():
    repeats = []
    with open("./day_3_input.txt", "r") as f:
        group = []
        for i, line in enumerate(f):
            group.append(line)

            if (i+1) % 3 != 0:
                continue

            for item in group[0]:
                if item in group[1] and item in group[2]:
                    ascii = ord(item)
                    repeats.append(ascii - 96 if ascii >= 97 else ascii - 38)
                    break
            group = []

    return sum(repeats)


if __name__ == '__main__':
    print()
    print('--- DAY 3 ---')
    print('1.', pt1())
    print('2.', pt2())
    print()
