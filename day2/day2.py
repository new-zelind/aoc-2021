# part 1

input = open('input.txt', 'r')

data = input.readlines()

horiz = 0
depth = 0

for i in data:

    i.strip()
    curr = i.split()

    if curr[0] == "down":
        depth += int(curr[1])
    elif curr[0] == "up":
        depth -= int(curr[1])
    else:
        horiz += int(curr[1])

print(horiz * depth)

# part 2

horiz = 0
depth = 0
aim = 0

for i in data:

    i.strip()
    curr = i.split()

    if curr[0] == "down":
        aim += int(curr[1])
    elif curr[0] == "up":
        aim -= int(curr[1])
    else:
        horiz += int(curr[1])
        depth += aim * int(curr[1])

print(horiz * depth)