range = list(range(1,99))

with open("day4inp.txt") as file:
    lines = file.readlines()

enclosed = 0
overlap = 0
for line in lines:
    elf1, elf2 = line.split(",")
    
    elf11, elf12 = elf1.split("-")
    
    elf21, elf22 = elf2.split("-")
    
    if int(elf11) < int(elf21): #means 2 is enclosed by 1 if at all
        if int(elf12) >= int(elf22): #means 2 is enclosed
            enclosed += 1
        elif int(elf21) <= int(elf12): #overlap
            overlap += 1
    elif int(elf11) > int(elf21): #means 1 is enclosed by 2 if at all
        if int(elf12) <= int(elf22): #means 1 is enclosed
            enclosed += 1
        elif (int(elf22) >= int(elf11)): #overlap
            overlap += 1
    else: #means they are equal and one will always enclose the other
        enclosed += 1

print(enclosed)
print(enclosed + overlap)
