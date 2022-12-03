total = []
with open('input', 'r') as f:
    sum = 0
    for line in f:
        if(len(line.rstrip()) == 0):
            total.append(sum)
            sum = 0
        else:
            sum += int(line.rstrip())

print(max(total))
