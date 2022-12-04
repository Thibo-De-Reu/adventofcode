total = []
with open('input', 'r') as f:
    temp = 0
    for line in f:
        if(len(line.rstrip()) == 0):
            total.append(temp)
            temp = 0
        else:
            temp += int(line.rstrip())

print(max(total))
