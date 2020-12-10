import pprint
from aocd.models import Puzzle
from aocd import submit
import time
import collections

puzzle = Puzzle(year=2020, day=8)

raw = puzzle.input_data
data = raw.splitlines()
data.append('')

accumulator = 0
i = 0
loop_list = []
while True:
    print(i)
    print(data[i])
    if i in loop_list:

        break
    loop_list.append(i)
    if 'nop' in data[i]:
        i += 1
    if 'acc' in data[i]:
        accumulator += int(data[i].split(' ')[1])
        i += 1
    if 'jmp' in data[i]:
        i = i + int(data[i].split(' ')[1])

print(loop_list)
print(accumulator)

# submit(total_count, part="b", day=6, year=2020)
