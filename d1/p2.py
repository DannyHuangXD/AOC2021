import sys

cnt_inc = 0
lines = []

with open("input.txt", "r+") as f:
    lines = f.readlines()

prv = sys.maxsize
for i, d in enumerate(lines):
    if i == len(lines) - 2:
        break
    
    cur =  int(d) + int(lines[i+1]) + int(lines[i+2])
    if prv < cur:
        cnt_inc += 1
    prv = cur

print(cnt_inc)
