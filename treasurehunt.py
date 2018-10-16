# -*- coding: utf-8 -*-

#Noah Smith Gunnar Nick
# Team Slytherin

#Lab 3  - Treasure Hunt

#import
import random


#Add a greeting.
#prompt for difficulty
    # 3x3, 4x4, 5x5
    
#RANDOMLY place treasure on grid
    #should be with two random integers in a list
    
#print where the user has already guessed
    
#Prompt when the user has guessed where the box is
    
#check if box is there
    
#check to see if there are any guesses left




grid3 = input('Please input the size of the grid you would like to use. (Please input 3x3, 4x4, or 5x5.)')
guessCount = 0

if grid3 == '3x3':
    guessCount = 5
elif grid3 == '4x4':
    guessCount = 10
elif grid3 == '5x5':
    guessCount = 15
    
while grid3 !='done':
    if grid3 == '3x3':
        grid3= [[1,2,3],[4,5,6],[7,8,9]]
        
        ans1 = random.randint(1,5)
        ans2 = random.randint(6,9)
        
        tres1 = ans1
        tres2 = ans2
        
        
        print(grid3)
        
        while guessCount!=0:
            guess= int(input('Please input guess. (X means treasure is not there,\n while O means the treasuer is there.)'))
            if guess in(1,2,3,4,5,6,7,8,9):
                #Number 1
                if guess==1 and guess==(ans1 or ans2):
                     grid3[0][0]='O'
                     print(grid3)
                elif guess==1 and guess!=(ans1 or ans2):
                    grid3[0][0]='X'
                    print(grid3)
                #Number 2
                elif guess==2 and guess==(ans1 or ans2):
                    grid3[0][1]='O'
                    print(grid3)
                elif guess==2 and guess!=(ans1 or ans2):
                    grid3[0][1]='X'
                    print(grid3)
                #Number 3
                elif guess==3 and guess==(ans1 or ans2):
                    grid3[0][2]='O'
                    print(grid3)
                elif guess==3 and guess!=(ans1 or ans2):
                    grid3[0][2]='X'
                    print(grid3)
                #Number 4
                elif guess==4 and guess==(ans1 or ans2):
                    grid3[1][0]='O'
                    print(grid3)
                elif guess==4 and guess!=(ans1 or ans2):
                    grid3[1][0]='X'
                    print(grid3)
                #Number 5
                elif guess==5 and guess==(ans1 or ans2):
                    grid3[1][1]='O'
                    print(grid3)
                elif guess==5 and guess!=(ans1 or ans2):
                    grid3[1][1]='X'
                    print(grid3)
                #Number 6
                elif guess==6 and guess==(ans1 or ans2):
                    grid3[1][2]='O'
                    print(grid3)
                elif guess==6 and guess!=(ans1 or ans2):
                    grid3[1][2]='X'
                    print(grid3)
                #Number 7
                elif guess==7 and guess==(ans1 or ans2):
                    grid3[2][0]='O'
                    print(grid3)
                elif guess==7 and guess!=(ans1 or ans2):
                    grid3[2][0]='X'
                    print(grid3)
                #Number 8
                elif guess==8 and guess==(ans1 or ans2):
                    grid3[2][1]='O'
                    print(grid3)
                elif guess==8 and guess!=(ans1 or ans2):
                    grid3[2][1]='X'
                    print(grid3)
                #Number 9
                elif guess==9 and guess==(ans1 or ans2):
                    grid3[2][2]='O'
                    print(grid3)
                elif guess==9 and guess!=(ans1 or ans2):
                    grid3[2][2]='X'
                    print(grid3)
            
                guessCount=guessCount-1
               
                
            else:
                print('Please input a correct guess.')
                int(input('Input a guess again.'))
                
        
    elif grid3 == '4x4':
        grid4= [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
        
        ans1 = random.randint(1,8)
        ans2 = random.randint(9,16)
        
        tres1 = ans1
        tres2 = ans2
        
        
        print(grid4)
        
        while guessCount!=0:
            guess= int(input('Please input guess. (X means treasure is not there,\n while O means the treasuer is there.)'))
            if guess in(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16):
                #Number 1
                if guess==1 and guess==(ans1 or ans2):
                    grid4[0][0]='O'
                    print(grid4)
                elif guess==1 and guess!=(ans1 or ans2):
                    grid4[0][0]='X'
                    print(grid4)
                #Number 2
                elif guess==2 and guess==(ans1 or ans2):
                    grid4[0][1]='O'
                    print(grid4)
                elif guess==2 and guess!=(ans1 or ans2):
                    grid4[0][1]='X'
                    print(grid4)
                #Number 3
                elif guess==3 and guess==(ans1 or ans2):
                    grid4[0][2]='O'
                    print(grid4)
                elif guess==3 and guess!=(ans1 or ans2):
                    grid4[0][2]='X'
                    print(grid4)
                #Number 4
                elif guess==4 and guess==(ans1 or ans2):
                    grid4[0][3]='O'
                    print(grid4)
                elif guess==4 and guess!=(ans1 or ans2):
                    grid4[0][3]='X'
                    print(grid4)
                #Number 5
                elif guess==5 and guess==(ans1 or ans2):
                    grid4[1][0]='O'
                    print(grid4)
                elif guess==5 and guess!=(ans1 or ans2):
                    grid4[1][0]='X'
                    print(grid4)
                #Number 6
                elif guess==6 and guess==(ans1 or ans2):
                    grid4[1][1]='O'
                    print(grid4)
                elif guess==6 and guess!=(ans1 or ans2):
                    grid4[1][1]='X'
                    print(grid4)
                #Number 7
                elif guess==7 and guess==(ans1 or ans2):
                    grid4[1][2]='O'
                    print(grid4)
                elif guess==7 and guess!=(ans1 or ans2):
                    grid4[1][2]='X'
                    print(grid4)
                #Number 8
                elif guess==8 and guess==(ans1 or ans2):
                    grid4[1][3]='O'
                    print(grid4)
                elif guess==8 and guess!=(ans1 or ans2):
                    grid4[1][3]='X'
                    print(grid4)
                #Number 9
                elif guess==9 and guess==(ans1 or ans2):
                    grid4[2][0]='O'
                    print(grid4)
                elif guess==9 and guess!=(ans1 or ans2):
                    grid4[2][0]='X'
                    print(grid4)
                #Number 10
                elif guess==10 and guess==(ans1 or ans2):
                    grid4[2][1]='O'
                    print(grid4)
                elif guess==10 and guess!=(ans1 or ans2):
                    grid4[2][1]='X'
                    print(grid4)
                #Number 11
                elif guess==11 and guess==(ans1 or ans2):
                    grid4[2][2]='O'
                    print(grid4)
                elif guess==11 and guess!=(ans1 or ans2):
                    grid4[2][2]='X'
                    print(grid4)
                #Number 12
                elif guess==12 and guess==(ans1 or ans2):
                    grid4[2][3]='O'
                    print(grid4)
                elif guess==12 and guess!=(ans1 or ans2):
                    grid4[2][3]='X'
                    print(grid4)
                #Number 13
                elif guess==13 and guess==(ans1 or ans2):
                    grid4[3][0]='O'
                    print(grid4)
                elif guess==13 and guess!=(ans1 or ans2):
                    grid4[3][0]='X'
                    print(grid4)
                #Number 14
                elif guess==14 and guess==(ans1 or ans2):
                    grid4[3][1]='O'
                    print(grid4)
                elif guess==14 and guess!=(ans1 or ans2):
                    grid4[3][1]='X'
                    print(grid4)
                #Number 15
                elif guess==15 and guess==(ans1 or ans2):
                    grid4[3][2]='O'
                    print(grid4)
                elif guess==15 and guess!=(ans1 or ans2):
                    grid4[3][2]='X'
                    print(grid4)
                #Number 16
                elif guess==16 and guess==(ans1 or ans2):
                    grid4[3][3]='O'
                    print(grid4)
                elif guess==16 and guess!=(ans1 or ans2):
                    grid4[3][3]='X'
                    print(grid4)   
                guessCount=guessCount-1
                
            else:
                print('Please input a correct guess.')
                int(input('Input a guess again.'))


        
    elif grid3 == '5x5':
        grid5= [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
        
        ans1 = random.randint(1,16)
        ans2 = random.randint(17,25)
        
        tres1 = ans1
        tres2 = ans2
        
        
        print(grid5)

        while guessCount!=0:
            guess= int(input('Please input guess. (X means treasure is not there,\n while O means the treasuer is there.)'))
            if guess in(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25):
                #Number 1
                if guess==1 and guess==(ans1 or ans2):
                    grid5[0][0]='O'
                    print(grid5)
                elif guess==1 and guess!=(ans1 or ans2):
                    grid5[0][0]='X'
                    print(grid5)
                #Number 2
                elif guess==2 and guess==(ans1 or ans2):
                    grid5[0][1]='O'
                    print(grid5)
                elif guess==2 and guess!=(ans1 or ans2):
                    grid5[0][1]='X'
                    print(grid5)
                #Number 3
                elif guess==3 and guess==(ans1 or ans2):
                    grid5[0][2]='O'
                    print(grid5)
                elif guess==3 and guess!=(ans1 or ans2):
                    grid5[0][2]='X'
                    print(grid5)
                #Number 4
                elif guess==4 and guess==(ans1 or ans2):
                    grid5[0][3]='O'
                    print(grid5)
                elif guess==4 and guess!=(ans1 or ans2):
                    grid5[0][3]='X'
                    print(grid5)
                #Number 5
                elif guess==5 and guess==(ans1 or ans2):
                    grid5[0][4]='O'
                    print(grid5)
                elif guess==5 and guess!=(ans1 or ans2):
                    grid5[0][4]='X'
                    print(grid5)
                #Number 6
                elif guess==6 and guess==(ans1 or ans2):
                    grid5[1][0]='O'
                    print(grid5)
                elif guess==6 and guess!=(ans1 or ans2):
                    grid5[1][0]='X'
                    print(grid5)
                #Number 7
                elif guess==7 and guess==(ans1 or ans2):
                    grid5[1][1]='O'
                    print(grid5)
                elif guess==7 and guess!=(ans1 or ans2):
                    grid5[1][1]='X'
                    print(grid5)
                #Number 8
                elif guess==8 and guess==(ans1 or ans2):
                    grid5[1][2]='O'
                    print(grid5)
                elif guess==8 and guess!=(ans1 or ans2):
                    grid5[1][2]='X'
                    print(grid5)
                #Number 9
                elif guess==9 and guess==(ans1 or ans2):
                    grid5[1][3]='O'
                    print(grid5)
                elif guess==9 and guess!=(ans1 or ans2):
                    grid5[1][3]='X'
                    print(grid5)
                #Number 10
                elif guess==10 and guess==(ans1 or ans2):
                    grid5[1][4]='O'
                    print(grid5)
                elif guess==10 and guess!=(ans1 or ans2):
                    grid5[1][4]='X'
                    print(grid5)
                #Number 11
                elif guess==11 and guess==(ans1 or ans2):
                    grid5[2][0]='O'
                    print(grid5)
                elif guess==11 and guess!=(ans1 or ans2):
                    grid5[2][0]='X'
                    print(grid5)
                #Number 12
                elif guess==12 and guess==(ans1 or ans2):
                    grid5[2][1]='O'
                    print(grid5)
                elif guess==12 and guess!=(ans1 or ans2):
                    grid5[2][1]='X'
                    print(grid5)
                #Number 13
                elif guess==13 and guess==(ans1 or ans2):
                    grid5[2][2]='O'
                    print(grid5)
                elif guess==13 and guess!=(ans1 or ans2):
                    grid5[2][2]='X'
                    print(grid5)
                #Number 14
                elif guess==14 and guess==(ans1 or ans2):
                    grid5[2][3]='O'
                    print(grid5)
                elif guess==14 and guess!=(ans1 or ans2):
                    grid5[2][3]='X'
                    print(grid5)
                #Number 15
                elif guess==15 and guess==(ans1 or ans2):
                    grid5[2][4]='O'
                    print(grid5)
                elif guess==15 and guess!=(ans1 or ans2):
                    grid5[2][4]='X'
                    print(grid5)
                #Number 16
                elif guess==16 and guess==(ans1 or ans2):
                    grid5[3][0]='O'
                    print(grid5)
                elif guess==16 and guess!=(ans1 or ans2):
                    grid5[3][0]='X'
                    print(grid5)
                #Number 15
                elif guess==15 and guess==(ans1 or ans2):
                    grid5[3][1]='O'
                    print(grid5)
                elif guess==16 and guess!=(ans1 or ans2):
                    grid5[3][1]='X'
                    print(grid5)
                #Number 18 
                elif guess==15 and guess==(ans1 or ans2):
                    grid5[3][2]='O'
                    print(grid5)
                elif guess==16 and guess!=(ans1 or ans2):
                    grid5[3][2]='X'
                    print(grid5)
                #Number 19    
                elif guess==15 and guess==(ans1 or ans2):
                    grid5[3][3]='O'
                    print(grid5)
                elif guess==16 and guess!=(ans1 or ans2):
                    grid5[3][3]='X'
                    print(grid5)
                #Number 20    
                elif guess==15 and guess==(ans1 or ans2):
                    grid5[3][4]='O'
                    print(grid5)
                elif guess==16 and guess!=(ans1 or ans2):
                    grid5[3][4]='X'
                    print(grid5)
                #Number 21    
                elif guess==15 and guess==(ans1 or ans2):
                    grid5[4][0]='O'
                    print(grid5)
                elif guess==16 and guess!=(ans1 or ans2):
                    grid5[4][0]='X'
                    print(grid5)
                #Number 22
                elif guess==15 and guess==(ans1 or ans2):
                    grid5[4][1]='O'
                    print(grid5)
                elif guess==16 and guess!=(ans1 or ans2):
                    grid5[4][1]='X'
                    print(grid5)
                #Number 23
                elif guess==15 and guess==(ans1 or ans2):
                    grid5[4][2]='O'
                    print(grid5)
                elif guess==16 and guess!=(ans1 or ans2):
                    grid5[4][2]='X'
                    print(grid5)
                #Number 24    
                elif guess==15 and guess==(ans1 or ans2):
                    grid5[4][3]='O'
                    print(grid5)
                elif guess==16 and guess!=(ans1 or ans2):
                    grid5[4][3]='X'
                    print(grid5)
                #Number 25    
                elif guess==15 and guess==(ans1 or ans2):
                    grid5[4][4]='O'
                    print(grid5)
                elif guess==16 and guess!=(ans1 or ans2):
                    grid5[4][4]='X'
                    print(grid5)
                guessCount=guessCount-1
               
                
            else:
                print('Please input a correct guess.')
                int(input('Input a guess again.'))       
        
        
        
    elif grid3 not in ('3x3, 4x4, 5x5'):
        grid3 = input('Please input a valid level grid. (press enter)')
    grid3 = input('What level would you like to play? If you are done, type done.')
    



