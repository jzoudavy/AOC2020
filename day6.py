import pprint
from aocd.models import Puzzle

def process_customs_data(data):
    print(data)
    pass

puzzle = Puzzle(year=2020, day=6)

raw = puzzle.input_data
data = raw.splitlines()


customs_data = []

for line in data:

    if line == '':
        if (process_customs_data(customs_data)):
            customs_data = []

    else:
        customs_data.append(line.strip())


