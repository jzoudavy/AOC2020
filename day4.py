import pprint

passport_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
passport_data = []
valid_passport = 0
total_passports = 0
ecl_allowed = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
_hcl_char_allowed = ['a', 'b', 'c', 'd', 'e', 'f']
_hcl_num_allowed = []
for i in range(10):
    _hcl_num_allowed.append(str(i))


hcl_allowed = _hcl_num_allowed+ _hcl_char_allowed
print(hcl_allowed)
'''
list(range(9))


field_requirments = {
    'byr' : '1920 2020', #min max year
    'iyr' : '1920 2020',
    'eyr' : '2020 2030',
    'hgt' : '150 193 59 76', #min max cm min max in
    'hcl' : '#xxxxxx', # #with 6 alpha numeric
    'pid' : 'xxxxxxxxx' # 9 numeric with leading zeros
    'ecl' : ' amb blu brn gry grn hzl oth'
}
'''
f = open("day4_input.txt", "r")
#f = open("day4_example", "r")
data = f.readlines()


def check_fields(sanitized):
    print('='*50)
    pprint.pprint(sanitized)
    for field_name, field_value in sanitized.items():
        if 'byr' == field_name:
            if not (1920 <= int(field_value) <= 2002): return False
        if 'iyr' == field_name:
            if not (2010 <= int(field_value) <= 2020): return False
        if 'eyr' == field_name:
            if not (2020 <= int(field_value) <= 2030): return False
        if 'hgt' == field_name:
            if 'in' in field_value:
                if not (59 <= int(field_value[:-2]) <= 76): return False
            elif 'cm' in field_value:
                if not (150 <= int(field_value[:-2]) <= 193): return False
            else:
                return False
        if 'hcl' == field_name:
            if field_value[0] != '#': return False
            if len(field_value[1:]) != 6: return False
            for i in field_value[1:]:
                if i not in hcl_allowed: return False
        if 'pid' == field_name:
            if not (len(field_value) == 9 and field_value.isnumeric()): return False
        if 'ecl' == field_name:
            if field_value not in ecl_allowed: return False

    return True


def process_passport_data(passport_data):
    sanitized = {}

    for data in passport_data:
        if ' ' in data:  # we have multiple field lines
            for item in data.split(' '):
                sanitized[item.split(':')[0]] = item.split(':')[1]
        else:  # single field lines
            sanitized[data.split(':')[0]] = data.split(':')[1]

    for fields in passport_fields:
        if fields not in sanitized.keys(): return False
    if check_fields(sanitized):
        print("+"*50)
        return True
    else:
        print("-" * 50)
        return False


for line in data:
    if line == '\n':
        if (process_passport_data(passport_data)):
            valid_passport += 1

        passport_data = []
        total_passports += 1

    else:
        passport_data.append(line.strip())

print(valid_passport)
print(total_passports)
