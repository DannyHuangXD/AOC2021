import sys

cnt_inc = 0

with open("input.txt", "r+") as f:
    prv = sys.maxsize
    for line in f:
        if int(line) > prv:
            cnt_inc += 1
        prv = int(line)

    print(cnt_inc)
