###Bismilah ###
import random
###part1
matrix=[]
added=[]
volume=False
while volume==False:
    lines=int(input('Enter How Muh Lines you want! :'))
    columns=int(input('Enter How Muh columns you want! :'))
    if(lines and columns):
        volume=True;

for i in range(lines):
    row=[];
    for j in range(columns):
        # rand=random.randint(1,49)
        rand=int(input('Enter a number :'))
        while rand<1 or rand>49 or added.count(rand)==1:
            print("Error in Input..,Try Again!")
            rand=int(input('Enter a number again:'))
            # rand=random.randint(1,49)
        
        row.append(rand)
        added.append(rand)

    matrix.append(row)
###chosing players names
names=False
while names==False:
    player1=input(str('Gambler 1,Enter your Name:'))
    player2=input(str('Gambler 2,Enter your Name:'))
    if(len(player1)==0 or len(player2)==''):
        print('Empty! Must Enter Names Please')
    else:
        print('Names taken ,game will begin..!')
        names=True

z=0
end=False
countEnd=0
# player1='ABDELLATIF'
# player2='ISMAIL'
currentplayer=None
while end==False:
    
    print('matrix game',countEnd+1)
    for row  in matrix:
        print(row)

    xrand=rand=random.randint(1,49)
    if(countEnd==0):
        playerRand=random.choice([player1, player2])
        currentplayer=playerRand
    elif currentplayer==player1:
        currentplayer=player2
    else:
        currentplayer=player1

    print('xrand',xrand)
    print('Current Player is :',currentplayer)
    for z in range(xrand-3,xrand+3):
        print('should deleted:',z)
        for r in range(len(matrix)):
            row=[];
            for t in range(len(matrix[r])):
                if(matrix[r][t]!=z):
                    row.append(matrix[r][t]);
            matrix[r]=row; 


    print('Result Game :',countEnd+1)
    for row in matrix:
        print(row)
    if(matrix.count([])==len(matrix)):
        print('Last Result for game :',countEnd+1)
        for row in matrix:
            print(row)
        if currentplayer==player1:
            print('Winner is:',player1)
            print('Next Time maybe:',player2)
        else:
            print('Winner is :',player2)
            print('Next Time maybe:',player1)
        countEnd=countEnd+1
        end=True
    else:
        req=input(str('Wanna Continue?!,press Y/y :'))
        if req=='Y' or req=='y':
            countEnd=countEnd+1
        else:
            print('Last Result for game :',countEnd+1)
            for row in matrix:
                print(row)
            if currentplayer==player1:
                print('Hooray! The Winner is:',player1)
                print('Next Time maybe:',player2)
            else:
                print('Winner is :',player2)
                print('Next Time maybe:',player1)
            countEnd=countEnd+1
            break

print('X',countEnd,'Times')


### Made BY ABDELLATIF ###
    


