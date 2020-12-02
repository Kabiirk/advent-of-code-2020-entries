#Input
day1 = open("day1.txt", "r")

#each line in day1.txt -> each element of list as an integer
input_list = []
for line in day1:
    input_list.append(int(line))

sum = 2020
n = len(input_list) #Array Size

for i in range(0,n-1):
    s = set()
    temp = sum - input_list[i]

    for j in range(i+1,n):
        temp2 = temp-input_list[j]
        if (temp2 in s):
            print( str(input_list[i]) + " x " + str(input_list[j]) + " x " + str(temp2) + " = " + str(input_list[i]*input_list[j]*temp2))
        s.add(input_list[j])
day1.close()
