from functools import cache


def count_possible_positions(commands):

    positions = set()

    for i, command in enumerate(commands):
        prev_pos = commands[:i]
        next_pos = commands[i + 1:]

        if i == 0:
            prev_pos = ''
            next_pos = commands[i + 1:]
        elif i + 1 == len(commands):
            prev_pos = commands[:i]
            next_pos = ''

        if command == 'R':
            positions.add(count(prev_pos + 'F' + next_pos))
            positions.add(count(prev_pos + 'L' + next_pos))
        elif command == 'L':
            positions.add(count(prev_pos + 'R' + next_pos))
            positions.add(count(prev_pos + 'F' + next_pos))
        else:
            positions.add(count(prev_pos + 'R' + next_pos))
            positions.add(count(prev_pos + 'L' + next_pos))

    print(len(positions))


@cache
def count(commands):
    res = 0
    direct = 1

    for i in commands:
        if i == 'F':
            res += direct
        elif i == 'R':
            direct = 1
        else:
            direct = -1

    return res


n = int(input())
commands = input().strip()
count_possible_positions(commands)

