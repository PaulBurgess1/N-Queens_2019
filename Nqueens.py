import random
#global variable used everywhere
rows=[]
conflicts=[]
n = 0
#creates the starting board and calls the scramble function once
#so that it has a random starting state
def Board(_n):
    global rows
    global conflicts
    global n
    n = _n
    rows=[0]*n
    conflicts = [0]*n
    scramble()
#scrambles the board making sure its a random state
#this involves some strategy to make sure to minimize 
#starting conflicts 
def scramble():
    global rows
    global n
    for i in range(n):
        rows[i]=i
    for i in range(n):
        randT=random.randint(0,len(rows)-1)
        rowToSwap=rows[i]
        rows[i]=rows[randT]
        rows[randT]=rowToSwap
    for i in range(n):
        conflicts[i] = num_conflicts(rows[i], i)
#update the conflicts list based on new and old values, and the state to a chosen child
#state
def update_conflicts_and_row(oldRow, col, newRow,):
    global rows
    global conflicts
    global n
    newCount=0
    for i in range(n):
        if (i==col):
            continue
        r=rows[i]
        if(r==newRow or abs(r-newRow)==abs(i-col)):
	#update the new conflicts
            newCount+=1
            conflicts[i] += 1
        if(r==oldRow or abs(r-oldRow)==abs(i-col)):
	#remove the old conflicts
            conflicts[i] -= 1
    conflicts[col] = newCount
#update the state
    rows[col] = newRow
#calculate total conflicts for a queen that has the position
#of row and col
def num_conflicts(row, col):
    global rows
    count=0
    for i in range(len(rows)):
        if (i==col):
            continue
        r=rows[i]
        if(r==row or abs(r-row)==abs(i-col)):
            count+=1
    return count
#this is the actual hill climbing algorithm, it uses scramble function
#as well as the row array that is used globally  
def solve():
    #get the worst queen for swap
    global rows
    global conflicts
    global n
    moves=0
    while(True):
    #get the worst queen for swap
        maxConflicts=0
        candidates=[]
        for i in range(n):
            confli = conflicts[i]
            if confli==maxConflicts:
                candidates.append(i)
            elif confli>maxConflicts:
                maxConflicts=confli
                candidates.clear()
                candidates.append(i)
        if (maxConflicts==0):
            #print("done")
            return
        worstQueenCol=random.choice(candidates)
        minConflicts=n
        oldRow = rows[worstQueenCol]
        candidates.clear()
        for i in range(n):
            confli=num_conflicts(i, worstQueenCol)
            if confli == minConflicts:
                candidates.append(i)
            elif confli<minConflicts:
                minConflicts=confli
                candidates.clear()
                candidates.append(i)
        newRow=random.choice(candidates)
        update_conflicts_and_row(oldRow, worstQueenCol, newRow)
        moves+=1
        if moves == len(rows)*2:
            scramble()
            moves=0

size =input("Please enter a board size.(Integer, >= 8)")
Board(int(size))
solve()
for i in range(len(rows)):
    print((" o "*rows[i]+' X '+' o '*(len(rows)-rows[i]-1)))
