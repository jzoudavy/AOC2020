import pprint

f = open("day3_input.txt", "r")
data =f.readlines()



def get_trees(x_step, y_step):
    trees = 0
    for y in range(0,len(data),y_step):
        x = int(y/y_step * x_step)
        print(y,x)
        #print(len(data[0])) is 32
        print(x%len(data[0]))
        if( data[y][x%31] == '#'): trees = trees+ 1
    return trees

part_a = get_trees(3,1)
print(part_a)
'''
length =3
width =1

for index_row, row in enumerate(lines):
    row = (row.strip())*100+'\n'
    lines[index_row] = row

pprint.pprint(lines)

for index_row, row in enumerate(lines):

    #print(lines[index_row+width][index_row*length+1])
    print((index_row+width),(index_row*length))
    if (index_row+1) == len(lines): break
    if lines[index_row+width][index_row*length] == '#':
        trees = trees+1


print(trees)
'''