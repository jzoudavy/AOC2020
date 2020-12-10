import pprint
from aocd.models import Puzzle
from aocd import submit
import time
import collections


def part2(array, next_num):
    # part 2
    found=False
    j =0
    loopsize=len(array)

    while j < loopsize:
        contigous_list = []
        contigous_sum = 0

        for item in array:
            if contigous_sum == next_num and len(contigous_list) > 2:
                found= True
                print(max(contigous_list) + min(contigous_list))
                break


            else:
                #print(contigous_sum)
                contigous_sum += item
                contigous_list.append(item)
                #print(contigous_list)
        if found == True:
            print(contigous_list)
            break
        array.pop(0)
        j+=1


def rulecheck(array):
    next_num = array[-1]
    array.pop(-1)
    for i in array:
        for j in array:
            if i+j == next_num: return False


    return True



puzzle = Puzzle(year=2020, day=9)

raw = puzzle.input_data
data = raw.splitlines()
#f = open("day9_sample", "r")
#data = f.readlines()

for i in range(0, len(data)):
    data[i] = int(data[i].strip())

original = data.copy()
preamble = 25

while not rulecheck(data[:(preamble+1)]):
    data.pop(0)

#127 for sample
#1038347917 for actual puzzel
part2(original, 1038347917)



# submit(total_count, part="b", day=6, year=2020)
