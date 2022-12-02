def part1():
    #win = 6, draw = 3, loss = 0
    #rock (A,X) = 1, paper (B,Y) = 2, scissors (C,Z) = 3

    with open("day2inp.txt") as file:
        lines = file.readlines()
    file.close()
    x = 0
    for line in lines:
        if ((line[0] == "A") and (line[2] == "X")): #rock draw
            x += (1+3) #1 for rock, 3 for draw
        elif ((line[0] == "B") and (line[2] == "X")): #rock loss
            x += (1+0) #1 for rock, 0 for loss
        elif ((line[0] == "C") and (line[2] == "X")): #rock win
            x += (1+6) #1 for rock, 6 for win
        elif ((line[0] == "B") and (line[2] == "Y")): #paper draw
            x += (2+3) #2 for paper, 3 for draw
        elif ((line[0] == "C") and (line[2] == "Y")): #paper loss
            x += (2+0) #2 for paper, 0 for loss
        elif ((line[0] == "A") and (line[2] == "Y")): #paper win
            x += (2+6) #2 for paper, 6 for win
        elif ((line[0] == "C") and (line[2] == "Z")): #scissor draw
            x += (3+3) #3 for scissors, 3 for draw
        elif ((line[0] == "A") and (line[2] == "Z")): #scissor loss
            x += (3+0) #3 for scissors, 0 for loss
        elif ((line[0] == "B") and (line[2] == "Z")): #scissor win
            x += (3+6) #3 for scissors, 6 for win
    print(x)
    
    
def part2():
    #win = 6, draw = 3, loss = 0
    #opponent: rock (A), paper (B), scissors (C)
    #you: need to lose (X), need to draw (Y), need to win (Z)
    with open("day2inp.txt") as file:
        lines = file.readlines()
    file.close()
    x = 0
    for line in lines:
        if ((line[0] == "A") and (line[2] == "X")): #opponenet rock, need to lose, choose scissors
            x += (3+0) #3 for scissors, 0 for loss
        elif ((line[0] == "B") and (line[2] == "X")): #opponent paper, need to lose, choose rock
            x += (1+0) #1 for rock, 0 for loss
        elif ((line[0] == "C") and (line[2] == "X")): #opponenet scissors, need to lose, choose paper
            x += (2+0) #2 for paper, 0 for loss
        elif ((line[0] == "A") and (line[2] == "Y")): #opponenet rock, need to draw, choose rock
            x += (1+3) #1 for rock, 3 for draw
        elif ((line[0] == "B") and (line[2] == "Y")): #opponent paper, need to draw, choose paper
            x += (2+3) #2 for paper, 3 for draw
        elif ((line[0] == "C") and (line[2] == "Y")): #opponent scissors, need to draw, choose scissors
            x += (3+3) #3 for scissors, 3 for draw
        elif ((line[0] == "A") and (line[2] == "Z")): #opponent rock, need to win, choose paper
            x += (2+6) #2 for paper, 6 for win
        elif ((line[0] == "B") and (line[2] == "Z")): #opponent paper, need to win, choose scissors
            x += (3+6) #3 for scissors, 6 for win
        elif ((line[0] == "C") and (line[2] == "Z")): #opponent scissors, need to win, choose rock
            x += (1+6) #1 for rock, 6 for win
    print(x)
    
    
part2()
