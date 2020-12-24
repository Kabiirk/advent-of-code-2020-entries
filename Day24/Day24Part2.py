'''
Coordinate system:
       / \     / \
     /     \ /     \
    |  0,-1 |  1,0  |
    |  nw   |  ne   |
   / \     / \     / \
 /     \ /     \ /     \
| -1,-1 |  0,0  |  1,1  |
|   w   |  ref  |   e   |
 \     / \     / \     /
   \ /     \ /     \ /
    | -1,0  |  0,1  |
    |  sw   |  se   |
     \     / \     /
       \ /     \ /
'''
# Part 1 code needed
def part1(tiles_list, direction):
    blacks = set()
    for line in tiles_list:
        i = 0
        steps = []
        while i < len(line):
            if line[i] == 's' or line[i] == 'n':
                steps.append(line[i: i+2])
                i = i + 2
            else:
                steps.append(line[i])
                i = i + 1

        x = 0
        y = 0
        for step in steps:
            x = x + direction[step][0]
            y = y + direction[step][1]
        if (x, y) not in blacks:
            blacks.add((x, y))
        else:
            blacks.remove((x, y))

    # Modified to save memory space
    return blacks


def part2(blacks, direction):
    day = 0
    while day < 100:
        cur_blacks = blacks.copy()
        for i in range(-200, 200, 1):
            if i % 2 == 0:
                js = [j for j in range(-202, 202, 2)]
            else:
                js = [j for j in range(-201, 202, 2)]
            for j in js:
                black_neighbors = 0
                for key in direction:
                    x = direction[key][0]
                    y = direction[key][1]
                    if (i+x, j+y) in blacks:
                        black_neighbors += 1

                if (i, j) in blacks:
                    if black_neighbors == 0 or black_neighbors > 2:
                        cur_blacks.remove((i, j))
                else:
                    if black_neighbors == 2:
                        cur_blacks.add((i, j))
        blacks = cur_blacks.copy()
        day = day + 1

    return len(blacks)



with open('day24.txt', 'r') as f:
    f = f.readlines()
    tiles_list = [line.strip() for line in f]

direction = {'nw':(-1, -1), 'sw':(1, -1), 'ne':(-1, 1),
                'se':(1, 1), 'w':(0, -2), 'e':(0, 2)}

blacks = part1(tiles_list, direction)
ans = part2(blacks, direction)
print(ans)