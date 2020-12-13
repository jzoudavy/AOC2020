import pprint
from aocd.models import Puzzle
from aocd import submit
import time
import collections
from itertools import groupby



puzzle = Puzzle(year=2020, day=11)

#raw = puzzle.input_data
#data = raw.splitlines()
f = open("day11_sample", "r")
data = f.readlines()


