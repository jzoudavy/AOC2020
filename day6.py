import pprint
from aocd.models import Puzzle
from aocd import submit
import time
import collections

def process_customs_data2(data, num_customers):
    if num_customers== 1:
        return len(set(data))
    else:
        c=collections.Counter(data)
        num_yes = 0
        for a in c:
            print(c[a])
            if c[a] == num_customers:
                num_yes +=1



        return num_yes


def process_customs_data(data):
    #print(data)
    return len(set(data))


puzzle = Puzzle(year=2020, day=6)

raw = puzzle.input_data
data = raw.splitlines()
data.append('')
#print(repr(data))
num_customers = 0
total_count = 0
customs_data = ""

for line in data:

    if line == '':
        total_count = total_count + process_customs_data2(customs_data, num_customers)
        customs_data = ''
        num_customers = 0
        #time.sleep(5)
    else:
        customs_data = customs_data + line.strip()
        num_customers = num_customers+1
        print(num_customers)

print(total_count)
submit(total_count, part="b", day=6, year=2020)
