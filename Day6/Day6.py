file = open("day6.txt","r")
productsFile = file.read()

grp_answers = productsFile.split("\n\n")
ques_ans = []

for grp_answer in grp_answers:
    ques_ans.append(len(set(list(grp_answer.replace("\n","")))))

print(sum(ques_ans))