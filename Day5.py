stacks = [[], [], [], [], [], [], [], [], []] #9 stacks

#stack.insert(0, item)
#stack.pop(0) AFTER x = stack[0]
#things with letters: ((x*4)-3)

def part1():
    with open("day5inp.txt") as file:
        lines = file.readlines()
    x = 0
    while x <= 7:
        line = lines[x]
        y = 1
        z = 0
        while y <= 33:
            if line[y] != " ":
                stacks[z].append(line[y])
            y += 4
            z += 1
        x += 1
    
    print(stacks)
    x = 10
    while x < len(lines):
        line = (lines[x].strip()).split(" ")
        while int(line[1]) > 0:  
            oldrow = int(line[3])-1
            newrow = int(line[5])-1 
            a = stacks[oldrow][0]
            stacks[oldrow].pop(0)
            stacks[newrow].insert(0, a)
            
            newInt = int(line[1])-1
            line[1] = str(newInt)       
        x+=1
        
    x = 0
    print(stacks)
    while x <= 8:
        print(stacks[x][0])
        x+=1
    
        
def part2():    
    with open("day5inp.txt") as file:
        lines = file.readlines()
    x = 0
    while x <= 7:
        line = lines[x]
        y = 1
        z = 0
        while y <= 33:
            if line[y] != " ":
                stacks[z].append(line[y])
            y += 4
            z += 1
        x += 1 
    
    x = 10
    while x < len(lines):
        line = (lines[x].strip()).split(" ")
        while int(line[1]) > 0:  
            oldrow = int(line[3])-1
            newrow = int(line[5])-1 
            a = stacks[oldrow][int(line[1])-1]
            stacks[oldrow].pop(int(line[1])-1)
            stacks[newrow].insert(0, a)
    
            newInt = int(line[1])-1
            line[1] = str(newInt)       
        x+=1
        
    x = 0
    print(stacks)
    while x <= 8:
        print(stacks[x][0])
        x+=1
    
        
part2()
