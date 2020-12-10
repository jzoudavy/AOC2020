import pprint
from aocd.models import Puzzle
from aocd import submit
import time
import collections

puzzle = Puzzle(year=2020, day=8)

raw = puzzle.input_data
data = raw.splitlines()
data.append('\n')

def part1(data, i, loop_list, accumulator):
    while True:
        if 'nop' in data[i]:
            i += 1
        if 'acc' in data[i]:
            accumulator += int(data[i].split(' ')[1])
            i += 1
        if 'jmp' in data[i]:
            i = i + int(data[i].split(' ')[1])

        if i in loop_list:
            return False
        if i == 622:
            return True

        loop_list.append(i)


def part2(data):

    for k,j in enumerate(data):
        accumulator = 0
        i = 0
        loop_list = []

        if 'nop' in j: j = j.replace('nop', 'jmp')
        if 'jmp' in j: j = j.replace('jmp', 'nop')

        data[k]=j
        print('new list sent')
        if (part1(data, i, loop_list, accumulator)): break
        else:
            print('shit '+str(k))


accumulator = 0
i = 0
loop_list = []

#part1(data, i, loop_list, accumulator)

part2(data)

# submit(total_count, part="b", day=6, year=2020)
