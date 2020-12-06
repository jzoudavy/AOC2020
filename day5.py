import pprint








def split_list(a_list):
    half = len(a_list)//2
    return a_list[:half], a_list[half:]


def determine_row(row_data):
    total_rows = range(128)
    for i in row_data:
        if 'F' == i:
            total_rows,_=split_list(total_rows)

        if 'B' == i:
            _, total_rows=split_list(total_rows)


    return total_rows[0]

def determine_col(col_data):
    total_col = range(8)
    for i in col_data:
        if 'R' == i:
            _, total_col = split_list(total_col)

        if 'L' == i:
            total_col, _ = split_list(total_col)

    return total_col[0]

def process_boarding_pass(line):
    row=determine_row(line[:7])
    col=determine_col(line[7:])

    return row*8+col





def part2(all_seat_id):
    all_seat_id=sorted(all_seat_id)
    for index, id in enumerate(all_seat_id):
        if all_seat_id[index+1]-all_seat_id[index] == 2:
            return id+1



f = open("day5_input.txt", "r")
#f = open("day5_example", "r")
data = f.readlines()

all_seat_id=[]


for line in data:
    line=line.strip()
    all_seat_id.append(int(process_boarding_pass(line)))


print(part2(all_seat_id))


