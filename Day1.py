#Input
day1 = open("input_data/day1.txt", "r")

#each line in day1.txt -> each element of list as an integer
input_list = []
for line in day1:
    input_list.append(int(line))

sum = 2020

s = set()

for i in input_list:
    temp = sum-i
    if(temp in s):
        print(str(i) + " + " + str(temp) + " = " + str(temp*i) )
    s.add(i)
