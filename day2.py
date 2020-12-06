
def password_check_part1(policy_min, policy_max, policy_char, password):
    print(policy_min, policy_max, policy_char, password)
    if int(policy_min)<= password.count(policy_char) <= int(policy_max):
        return 1


    return 0

def password_check_part2(policy_index1, policy_index2, policy_char, password):
    policy_index1= int(policy_index1)-1
    policy_index2= int(policy_index2)-1
    if password[policy_index1] == policy_char or password[policy_index2] == policy_char:
        if password[policy_index2] != password[policy_index1]:
            return 1


    return 0


f = open("day2_input.txt", "r")
lines =f.readlines()
valid_count=0
for i in lines:
    policy= i.split(':')[0]
    policy_min = policy.split(' ')[0].split('-')[0]
    policy_max = policy.split(' ')[0].split('-')[1]
    policy_char = policy.split(' ')[1]
    password=i.split(':')[1].strip()
    if password_check_part2(policy_min, policy_max, policy_char, password) == 1:
        valid_count= valid_count+1
    print(valid_count)

