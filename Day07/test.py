from collections import defaultdict, deque

line = "pale cyan bags contain 2 posh black bags, 4 wavy gold bags, 2 vibrant brown bags."

rules = {}
s = line.strip().split(' bags contain ')

content = defaultdict(int)

for comp in s[1].split(', '):
    words = comp.split(' ')
    if words[0] != 'no':
        content[words[1] + ' ' + words[2]] = int(words[0])
rules[s[0]] = content

bags = set(['shiny gold'])
l = 0
print("bags: ", bags)

while len(bags) > l:
    l = len(bags)
    # Iterate over the rules, if the rule contains anything in the set bags, add the key for that rule to the set bags
    [bags.add(key) for key in rules if any(color in rules[key].keys() for color in bags)]
print(bags)

print(f'Answer part 1: {len(bags)-1}')