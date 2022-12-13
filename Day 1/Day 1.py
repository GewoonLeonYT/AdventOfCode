with open("input.txt", 'r') as f:
    input = f.read().splitlines()
elvesInventory = [[int(j) for j in i.split(' ')] for i in ' '.join(input).split('  ')]
most = 0
firstPlace = 0
secondPlace = 0
thirdPlace = 0
for i in range(3):
    for j in elvesInventory:
        total = 0
        for k in j:
            total += k
        if most < total:
            most = total
            indexMost = elvesInventory.index(j)
    del elvesInventory[indexMost]
    indexMost = 0
    if firstPlace == 0:
        firstPlace = most
    elif secondPlace == 0:
        secondPlace = most
    else:
        thirdPlace = most
    most = 0
print(f"1st place: {firstPlace}\n2nd place: {secondPlace}\n3rd place: {thirdPlace}")
print("Total: " + str(firstPlace + secondPlace + thirdPlace))