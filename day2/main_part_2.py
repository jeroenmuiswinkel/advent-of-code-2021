with open('data.txt') as f:
    directions = [direction.split(" ") for direction in f.readlines()]

aim = 0
forward = 0
downward = 0
for direction in directions:
    if direction[0].startswith("forward"):
        forward += int(direction[1])
        downward += aim * int(direction[1])
    elif (direction[0].startswith("down")):
        aim += int(direction[1])
    elif (direction[0].startswith("up")):
        aim -= int(direction[1])

print(f"forward: {forward}")
print(f"downward: {downward}")
print(f"multiplication {forward * downward}")