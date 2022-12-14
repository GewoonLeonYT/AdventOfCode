with open("input.txt", 'r') as f:
    input = f.read().splitlines()
strategyGuide = [i.split(' ') for i in input]
pointsPartOne = 0
pointsPartTwo = 0
for i in strategyGuide:
    firstLetter = i[0]
    secondLetter = i[1]
    match secondLetter:
        case 'X':
            pointsPartOne += 1
            match firstLetter:
                case 'A':
                    pointsPartOne += 3
                case 'B':
                    pointsPartOne += 0
                case 'C':
                    pointsPartOne += 6
        case 'Y':
            pointsPartOne += 2
            match firstLetter:
                case 'A':
                    pointsPartOne += 6
                case 'B':
                    pointsPartOne += 3
                case 'C':
                    pointsPartOne += 0
        case 'Z':
            pointsPartOne += 3
            match firstLetter:
                case 'A':
                    pointsPartOne += 0
                case 'B':
                    pointsPartOne += 6
                case 'C':
                    pointsPartOne += 3
for i in strategyGuide:
    enemyMove = i[0]
    result = i[1]
    match result:
        case 'X':
            pointsPartTwo += 0
            match enemyMove:
                case 'A':
                    pointsPartTwo += 3
                case 'B':
                    pointsPartTwo += 1
                case 'C':
                    pointsPartTwo += 2
        case 'Y':
            pointsPartTwo += 3
            match enemyMove:
                case 'A':
                    pointsPartTwo += 1
                case 'B':
                    pointsPartTwo += 2
                case 'C':
                    pointsPartTwo += 3
        case 'Z':
            pointsPartTwo += 6
            match enemyMove:
                case 'A':
                    pointsPartTwo += 2
                case 'B':
                    pointsPartTwo += 3
                case 'C':
                    pointsPartTwo += 1
print(f"The answer to part 1 is {pointsPartOne}")
print(f"The answer to part 2 is {pointsPartTwo}")