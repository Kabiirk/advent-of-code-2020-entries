file = open("day6.txt","r")
productsFile = file.read()

grp_answers = productsFile.split("\n\n")

def intersection_of_multiple_strings(l):
    setlist = [ set(i) for i in l ]
    common_ans = len(set.intersection(*setlist))
    return(common_ans)

for i in range(len(grp_answers)):
    grp_answers[i] = grp_answers[i].split("\n")

for j in range(len(grp_answers)):
    grp_answers[j] = intersection_of_multiple_strings(grp_answers[j])


print(sum(grp_answers))