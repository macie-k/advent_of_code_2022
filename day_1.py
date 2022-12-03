
def pt1():
    max = 0

    with open("./day_1_input.txt", "r") as f:
        local_max = 0

        for line in f:
            if line.strip() == '':
                if local_max > max:
                    max = local_max
                local_max = 0
                continue

            local_max += int(line.strip())

    print(max)


def pt2():
    max3 = [0, 0, 0]
    with open("./day_1_input.txt", "r") as f:
        local_max = 0

        for line in f:
            if line.strip() == '':
                max3.sort()

                for i, max in enumerate(max3):
                    if local_max > max:
                        max3[i] = local_max
                        break

                local_max = 0
                continue

            local_max += int(line.strip())
    print(sum(max3))


if __name__ == '__main__':
    pt1()
    pt2()
