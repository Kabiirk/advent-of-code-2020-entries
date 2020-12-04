#open File
day4 = open("day4.txt", "r")

#combine all entries in 1 string
entries = ""
for line in day4:
    entries += line
day4.close()

#Split into list with empty line as delimiter which is essentially 2 newlines
passports = entries.split("\n\n") # => [password1, poassword2, ......]
fields = [ "byr", "iyr" , "eyr" ,"hgt" ,"hcl" ,"ecl" ,"pid"] #Fields present
counter = 0

#Count valid passwords
for passport in passports:
    passport.replace("\n", " ")
    if all(substring in passport for substring in fields): #Password validation condition as per question
        counter+=1
print(counter)