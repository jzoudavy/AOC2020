import pprint


passport_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
passport_data = []
valid_passport = 0
total_passports = 0


f = open("day4_input.txt", "r")
#f = open("day4_example", "r")
data = f.readlines()

def process_passport_data(passport_data):
    sanitized = {}

    for data in passport_data:
        if ' ' in data:  # we have multiple field lines
            for item in data.split(' '):

                sanitized[item.split(':')[0]] = item.split(':')[1]
        else:  # single field lines
            sanitized[data.split(':')[0]] = data.split(':')[1]
    pprint.pprint(sanitized)
    for fields in passport_fields:
        if fields not in sanitized.keys(): return False
    return True


for line in data:
    if line == '\n':
        if (process_passport_data(passport_data)):
            valid_passport += 1


        passport_data = []
        total_passports += 1

    elif data.index(line) == (len(data)-1):
        passport_data.append(line.strip())
        if (process_passport_data(passport_data)):
            valid_passport += 1
    else:
        passport_data.append(line.strip())



print(valid_passport)
print(total_passports)
