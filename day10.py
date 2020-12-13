import pprint
from aocd.models import Puzzle
from aocd import submit
import time
import collections
from itertools import groupby


def find_jolt_diff(a, b):
    # print(a,b)
    return b - a


jolt_diff_list = []

puzzle = Puzzle(year=2020, day=10)

raw = puzzle.input_data
data = raw.splitlines()
#f = open("day10_sample", "r")
#data = f.readlines()
data.append(str(0))

# make it into an array of ints
array = list(map(int, data))
device_jolt = max(array) + 3
array.append(device_jolt)
array.sort()
'''
# for part 1
print(array)
for index, jolt in enumerate(array):
    if (index + 1 == len(array)):
        break
    else:
        jolt_diff_list.append(find_jolt_diff(array[index], array[index + 1]))

print((collections.Counter(jolt_diff_list).values()))
'''
# for part 2

paths = collections.defaultdict(int)
paths[0] = 1
max_voltage= array[-1]
for adapter in sorted(array):
    for diff in range(1, 4):
        next_adapter = adapter + diff
        if next_adapter in array:
            paths[next_adapter] += paths[adapter]
print(paths[max_voltage])