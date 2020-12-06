'''
with open('input.txt') as fp:
    lines = fp.readlines()
    lines2 = lines
    lines3 = lines
    for i in lines:
        for j in lines2:
            for k in lines3:
            #print('i is :'+i)
            #print('j is :'+j)
            #print('sum is '+str(int(i)+int(j)))
                if (int(i)+int(j)+int(k)) == 2020:
                    print(str(int(i)*int(j)*int(k)))
'''

f = open("input.txt", "r")
nums = [int(i) for i in f.readlines()]
target = 2020
for index, num in enumerate(nums):
    print(num)
    if (target - num) in nums:
        print(num * (target - num))
        print(index)
        print(target-num)
        break