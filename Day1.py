calorie = []

with open("day1inp.txt") as file:
    lines = file.readlines()
    x = 0 
    for line in lines:
        if line == "\n":
            calorie.append(x)
            x = 0
        else:
            x += int(line.strip())
file.close() #could have closed file earlier
calorie.sort(reverse = True)
print(calorie[0]) #outputs carrier with most calorie, solves part 1
print(int(calorie[0]+calorie[1]+calorie[2])) #sums 3 heaviest carriers, solves part 2
