total = 0
with open('input.txt') as f:
    previous = 0
    for line in f:
        if previous != 0:
            if int(line) > previous:
                total += 1
        previous = int(line)
print(total)