day4 = open("day4.txt", "r")

count = 0
entries = ""

for line in day4:
    entries += line
day4.close()

passports = entries.split("\n\n")
fields = [ "byr", "iyr" , "eyr" ,"hgt" ,"hcl" ,"ecl" ,"pid"]
counter = 0

for passport in passports:
    passport.replace("\n", " ")
    if all(substring in passport for substring in fields):
        counter+=1
print(counter)
