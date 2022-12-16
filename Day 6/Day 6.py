with open('input.txt', 'r') as f:
    input = f.read()
signal = input

def checkRepeat(a: str) -> bool:
    for i in a:
        if a.count(i) > 1:
            return True
    return False
def searchMarker(a: str, b: int) -> int:
    for i in range(len(a)+1):
        currentNumber = i+b
        signalSegment = a[i:i+b]
        if checkRepeat(signalSegment) == False:
            return currentNumber

print(f"First start-of-packet marker starts at {searchMarker(signal, 4)}")
print(f"First start-of-message marker starts at {searchMarker(signal, 14)}")