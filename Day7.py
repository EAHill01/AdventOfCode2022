class myFile:
    def __init__(self, size, parent):
        self.size = size
        self.parent = parent

class dir:
    def __init__(self, name, size, line):
        self.name = name
        self.size = size
        self.line = line
        
    def getName(self):
        return self.name
        
    def updateSize(self, size):
        self.size += int(size)

    def getSize(self):
        return int(self.size)
        
pastParents = []
directories = []
files = [] #do i need to access files later?

with open("day7inp.txt") as file:
    lines = file.readlines()
    
for line in lines:
    split = (line.strip()).split(" ")
    #$ is command
    if split[0] == "$":
        if split[1] == "cd":
            if split[2] == "..":
                size = pastParents[len(pastParents)-1].getSize()
                pastParents.pop() #changes current parent directory
                pastParents[len(pastParents)-1].updateSize(size) #adds previous directories size to parent
            else:
                pastParents.append(dir(split[2], 0, "NA")) #now in this directory
                directories.append(pastParents[-1]) #allows access later
        elif split[1] == "ls":
            #do nothing here just yet?
            pass
    elif split[0] == "dir": #new directory not yet entered
        #do nothing assuming that every directory in the code is entered
        pass
    else: #file
        newFile = myFile(split[0], (pastParents[-1]).getName()) #do i even need to make a file for this?
        files.append(newFile)
        pastParents[-1].updateSize(split[0]) #adds file directly to parent size
print(pastParents)


while len(pastParents) != 1:
    size = pastParents[len(pastParents)-1].getSize()
    pastParents.pop() #changes current parent directory
    pastParents[len(pastParents)-1].updateSize(size) #adds previous directories size to parent

y = 0      
for x in directories:
    if x.getSize() <= 100000:
        y += x.getSize()
        
print(y)

a = 70000000 - directories[0].getSize()  #the unused space  
print(a)
y = 70000000  
for x in directories:
    if (x.getSize() >= (30000000-a)) and (y > x.getSize()): #30000000 - a is the space we need to find
        y = x.getSize()
        
print(y)
