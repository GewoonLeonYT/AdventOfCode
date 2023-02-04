with open("input.txt", 'r') as f:
    input = f.read().splitlines()
backpack = input
backpackCompartments = [[i[:len(i)//2], i[len(i)//2:]] for i in backpack]
backpackGroups = [backpack[i:i+3] for i in range(0, len(backpack), 3)]
sumPriorityCompartments = 0
sumPriorityGroups = 0

for i in backpackCompartments:
    lettersInCommon = set.intersection(set(i[0]), set(i[1]))
    for j in lettersInCommon:
        if j == j.lower():
            sumPriorityCompartments += ord(j) - 0x60
        else:
            sumPriorityCompartments += ord(j) - 0x26

for i in backpackGroups:
    lettersInCommon = set.intersection(set(i[0]), set(i[1]), set(i[2]))
    for j in lettersInCommon:
        if j == j.lower():
            sumPriorityGroups += ord(j) - 0x60
        else:
            sumPriorityGroups += ord(j) - 0x26
print(f"The sum of the priorities is {sumPriorityCompartments}")
print(f"The sum of the priorities of the groups is {sumPriorityGroups}")