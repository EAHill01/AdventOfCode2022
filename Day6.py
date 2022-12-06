with open("day6inp.txt") as file:
    line = file.readline()
    
    char = [0,0,0,0,0,0,0,0,0,0,0,0,0,0] #reduce to 4 for part1
    count = 0
    for x in line:
        char[13] = x #reduce to 3 for part 1
        if char[0] != 0:
            if ((len(char) > len(set(char))) == False):
                print(char)
                print(count+1)
                break
        i = 0
        while i < 13: #reduce to 3 for part 1
            char[i] = char[i+1]
            i+=1
        count+=1
