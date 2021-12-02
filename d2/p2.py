import sys

x_pos = 0
y_pos = 0
aim = 0

with open("input.txt", "r+") as f:
    for line in f:
        direction = line.split()
        print(f'{direction[0]}: {direction[1]}')
        if direction[0] == 'forward':
            x_pos += int(direction[1])
            y_pos += aim * int(direction[1])
        elif direction[0] == 'up':
            aim -= int(direction[1])
        elif direction[0] == 'down':
            aim += int(direction[1])
            
print(x_pos * y_pos)