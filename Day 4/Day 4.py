with open("input.txt", 'r') as f:
    input = f.read().splitlines()
indices = [[int(j) for j in i.replace('-', ',').split(',')] for i in input]
numFullyContains = 0
numOverlap = 0

def containChecker(a, b) -> bool:
    if len(a) > len(b):
        n = len(b)
        return any(b == a[i:i + n] for i in range(len(a)-n + 1))
    else:
        n = len(a)
        return any(a == b[i:i + n] for i in range(len(b)-n + 1))
def overlapChecker(a, b) -> bool:
    for i in a:
        if i in b:
            return True
    return False

for i in indices:
    elf1 = range(i[0], i[1]+1)
    elf2 = range(i[2], i[3]+1)    
    if containChecker(elf1, elf2):
        numFullyContains += 1

for i in indices:
    elf1 = range(i[0], i[1]+1)
    elf2 = range(i[2], i[3]+1)
    if overlapChecker(elf1, elf2):
        numOverlap += 1

print(f"Amount of assignment pairs that fully contain each other: {numFullyContains}")
print(f"Amount of assignment pairs that overlap with each other: {numOverlap}")