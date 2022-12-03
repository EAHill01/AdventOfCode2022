valueToIndex = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

def part1():
    with open("day3inp.txt") as file:
        lines = file.readlines()
        
    shared = ""
    for line in lines:
        part1 = ""
        part2 = ""
        batch = ""
        
        x = 0
        while x != (len(line.strip())/2):
            #first half
            part1 += line[x]
            x+=1
        while x != len(line.strip()):
            part2 += line[x]
            x+=1
        
        for y in part1:
            if (y in part2) and (y not in batch):
                shared += y
                batch += y

    value = 0
    for z in shared:
        value += (valueToIndex.index(z)+1)
    print(value)
    
    
    
def part2():
    with open("day3inp.txt") as file:
        lines = file.readlines()
        
    shared=""
    
    x = 2
    while x <= len(lines):
        for y in lines[x]:
            if (y in lines[x-1]) and (y in lines[x-2]):
                shared += y
                break
        x+=3
    
    value = 0
    for z in shared:
        value += (valueToIndex.index(z)+1)
    print(value)
    
    
part2()
