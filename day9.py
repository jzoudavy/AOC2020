import pprint
from aocd.models import Puzzle
from aocd import submit
import time
import collections

puzzle = Puzzle(year=2020, day=9)

raw = puzzle.input_data
data = raw.splitlines()

def part2(array, next_num):
    # part 2
    print(array)
    contigous_list = []
    contigous_sum = 0
    for i in array:
        if contigous_sum == next_num and len(contigous_list) > 2:
            print(max(contigous_list) + min(contigous_list))

        else:
            contigous_sum += i
            contigous_list.append(i)

    # part 2
def rulecheck(array):
    next_num = array[-1]
    array.pop(-1)
    for i in array:
        for j in array:
            if i+j == next_num: return False


    return True

f = open("day9_sample", "r")
data = f.readlines()

for i in range(0, len(data)):
    data[i] = int(data[i].strip())

print(len(data))
original = data
preamble = 5
while not rulecheck(data[:(preamble+1)]):
    data.pop(0)


print(original)

part2(original, 127)



# submit(total_count, part="b", day=6, year=2020)
