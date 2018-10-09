#Noah, Gunnar, Nick
# Team Slytherin

#Lab 2  - Calendar Project



# Greeting
#Variables listed
    #Var
#Get input
    #If else
    #loops
# Create Formating
# Output




import math as m

#greeting
print('Hey there and welcome to the calendar program! ')


#var list

year = int(input('What year are you looking for? 1800-2099 '))

while year < 1800 or year > 2099:
    year = input('Please input a corresponding year. 1800-2099: ')

century_digits = int(str(year)[:2])

year_digits = int(str(year)[-2:])

month = input('Please input a month. ex: Jan, Feb, Mar: ')
monthList = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']


while month not in monthList:
    month = input('Please input a correct month. ')

value = year_digits + m.floor(year_digits/4)




#Century Value Calulations
if century_digits == 18:
    value = value + 2
elif century_digits == 20:
    value = value + 6



#Month Value Calculations

if month == monthList[0] and (year%4 != 0):
    value= value +1
elif month == monthList[1] and (year%4 == 0):
    value= value +3
    if month == monthList[1] and (year%4 != 0):
        value= value +4
elif month == monthList[2] or month == monthList[10]:
    value= value +4
elif month == monthList[3] or month == monthList[6]:
    value= value +0
elif month == monthList[4]:
    value= value +2
elif month == monthList[5]:
    value= value +5
elif month == monthList[7]:
    value= value +3
elif month == monthList[9]:
    value= value +1
elif month == monthList[8] or month == monthList[11]:
    value= value +6
  


day = 0
#Days in month
if month == monthList[1]:
    if (year%4)==0:
        day = 29
    else:
        day = 28
        print('I am this one')
elif month in('Jan', 'Mar', 'May', 'Jul', 'Aug', 'Oct', 'Dec'):
    day = 31
    print('31 days!')
elif month in('Sep', 'Apr', 'Jun', 'Nov'):
    day = 30
    print('30 days!')

    

value = (value + 1) % 7




#Format!


headJan = format('-', '-<4'), 'January', format('-', '-<4')

headFeb = format('-', '-<4'), 'February', format('-', '-<4')

headMar = format('-', '-<4'), 'March', format('-', '-<4')

headApr = format('-', '-<4'), 'April', format('-', '-<4')

headMay = format('-', '-<4'), 'May', format('-', '-<4')

headJun = format('-', '-<4'), 'June', format('-', '-<4')

headJul = format('-', '-<4'), 'July', format('-', '-<4')

headAug = format('-', '-<4'), 'August', format('-', '-<4')

headSep = format('-', '-<4'), 'September', format('-', '-<4')

headOct = format('-', '-<4'), 'October', format('-', '-<4')

headNov = format('-', '-<4'), 'November', format('-', '-<4')

headDec = format('-', '-<4'), 'December', format('-', '-<4')


startSun28 = '[ 1][ 2][ 3][ 4][ 5][ 6][ 7]\n[ 8][ 9][10][11][12][13][14]\n[15][16][17][18][19][20][21]\n[22][23][24][25][26][27][28]'
startSun29 = '[ 1][ 2][ 3][ 4][ 5][ 6][ 7]\n[ 8][ 9][10][11][12][13][14]\n[15][16][17][18][19][20][21]\n[22][23][24][25][26][27][28]\n[29][  ][  ][  ][  ][  ][  ]'
startSun30 = '[ 1][ 2][ 3][ 4][ 5][ 6][ 7]\n[ 8][ 9][10][11][12][13][14]\n[15][16][17][18][19][20][21]\n[22][23][24][25][26][27][28]\n[29][30][  ][  ][  ][  ][  ]'
startSun31 = '[ 1][ 2][ 3][ 4][ 5][ 6][ 7]\n[ 8][ 9][10][11][12][13][14]\n[15][16][17][18][19][20][21]\n[22][23][24][25][26][27][28]\n[29][30][31][  ][  ][  ][  ]'
  
startMon28 = '[  ][ 1][ 2][ 3][ 4][ 5][ 6]\n[ 7][ 8][ 9][10][11][12][13]\n[14][15][16][17][18][19][20]\n[21][22][23][24][25][26][27]\n[28][  ][  ][  ][  ][  ][  ]'
startMon29 = '[  ][ 1][ 2][ 3][ 4][ 5][ 6]\n[ 7][ 8][ 9][10][11][12][13]\n[14][15][16][17][18][19][20]\n[21][22][23][24][25][26][27]\n[28][29][  ][  ][  ][  ][  ]'
startMon30 = '[  ][ 1][ 2][ 3][ 4][ 5][ 6]\n[ 7][ 8][ 9][10][11][12][13]\n[14][15][16][17][18][19][20]\n[21][22][23][24][25][26][27]\n[28][29][30][  ][  ][  ][  ]'
startMon31 = '[  ][ 1][ 2][ 3][ 4][ 5][ 6]\n[ 7][ 8][ 9][10][11][12][13]\n[14][15][16][17][18][19][20]\n[21][22][23][24][25][26][27]\n[28][29][30][31][  ][  ][  ]'

startTue28 = '[  ][  ][ 1][ 2][ 3][ 4][ 5]\n[ 6][ 7][ 8][ 9][10][11][12]\n[13][14][15][16][17][18][19]\n[20][21][22][23][24][25][26]\n[27][28][  ][  ][  ][  ][  ]'
startTue29 = '[  ][  ][ 1][ 2][ 3][ 4][ 5]\n[ 6][ 7][ 8][ 9][10][11][12]\n[13][14][15][16][17][18][19]\n[20][21][22][23][24][25][26]\n[27][28][29][  ][  ][  ][  ]'
startTue30 = '[  ][  ][ 1][ 2][ 3][ 4][ 5]\n[ 6][ 7][ 8][ 9][10][11][12]\n[13][14][15][16][17][18][19]\n[20][21][22][23][24][25][26]\n[27][28][29][30][  ][  ][  ]'
startTue31 = '[  ][  ][ 1][ 2][ 3][ 4][ 5]\n[ 6][ 7][ 8][ 9][10][11][12]\n[13][14][15][16][17][18][19]\n[20][21][22][23][24][25][26]\n[27][28][29][30][31][  ][  ]'

startWed28 = '[  ][  ][  ][ 1][ 2][ 3][ 4]\n[ 5][ 6][ 7][ 8][ 9][10][11]\n[12][13][14][15][16][17][18]\n[19][20][21][22][23][24][25]\n[26][27][28][  ][  ][  ][  ]'
startWed29 = '[  ][  ][  ][ 1][ 2][ 3][ 4]\n[ 5][ 6][ 7][ 8][ 9][10][11]\n[12][13][14][15][16][17][18]\n[19][20][21][22][23][24][25]\n[26][27][28][29][  ][  ][  ]'
startWed30 = '[  ][  ][  ][ 1][ 2][ 3][ 4]\n[ 5][ 6][ 7][ 8][ 9][10][11]\n[12][13][14][15][16][17][18]\n[19][20][21][22][23][24][25]\n[26][27][28][29][30][  ][  ]'
startWed31 = '[  ][  ][  ][ 1][ 2][ 3][ 4]\n[ 5][ 6][ 7][ 8][ 9][10][11]\n[12][13][14][15][16][17][18]\n[19][20][21][22][23][24][25]\n[26][27][28][29][30][31][  ]'

startThu28 = '[  ][  ][  ][  ][ 1][ 2][ 3]\n[ 4][ 5][ 6][ 7][ 8][ 9][10]\n[11][12][13][14][15][16][17]\n[18][19][20][21][22][23][24]\n[25][26][27][28][  ][  ][  ]'
startThu29 = '[  ][  ][  ][  ][ 1][ 2][ 3]\n[ 4][ 5][ 6][ 7][ 8][ 9][10]\n[11][12][13][14][15][16][17]\n[18][19][20][21][22][23][24]\n[25][26][27][28][29][  ][  ]'
startThu30 = '[  ][  ][  ][  ][ 1][ 2][ 3]\n[ 4][ 5][ 6][ 7][ 8][ 9][10]\n[11][12][13][14][15][16][17]\n[18][19][20][21][22][23][24]\n[25][26][27][28][29][30][  ]'
startThu31 = '[  ][  ][  ][  ][ 1][ 2][ 3]\n[ 4][ 5][ 6][ 7][ 8][ 9][10]\n[11][12][13][14][15][16][17]\n[18][19][20][21][22][23][24]\n[25][26][27][28][29][30][31]'

startFri28 = '[  ][  ][  ][  ][  ][ 1][ 2]\n[ 3][ 4][ 5][ 6][ 7][ 8][ 9]\n[10][11][12][13][14][15][16]\n[17][18][19][20][21][22][23]\n[24][25][26][27][28][  ][  ]'
startFri29 = '[  ][  ][  ][  ][  ][ 1][ 2]\n[ 3][ 4][ 5][ 6][ 7][ 8][ 9]\n[10][11][12][13][14][15][16]\n[17][18][19][20][21][22][23]\n[24][25][26][27][28][29][  ]'
startFri30 = '[  ][  ][  ][  ][  ][ 1][ 2]\n[ 3][ 4][ 5][ 6][ 7][ 8][ 9]\n[10][11][12][13][14][15][16]\n[17][18][19][20][21][22][23]\n[24][25][26][27][28][29][30]'
startFri31 = '[  ][  ][  ][  ][  ][ 1][ 2]\n[ 3][ 4][ 5][ 6][ 7][ 8][ 9]\n[10][11][12][13][14][15][16]\n[17][18][19][20][21][22][23]\n[24][25][26][27][28][29][30]\n[31][  ][  ][  ][  ][  ][  ]'

startSat28 = '[  ][  ][  ][  ][  ][  ][ 1]\n[ 2][ 3][ 4][ 5][ 6][ 7][ 8]\n[ 9][10][11][12][13][14][15]\n[16][17][18][19][20][21][22]\n[23][24][25][26][27][28][  ]'
startSat29 = '[  ][  ][  ][  ][  ][  ][ 1]\n[ 2][ 3][ 4][ 5][ 6][ 7][ 8]\n[ 9][10][11][12][13][14][15]\n[16][17][18][19][20][21][22]\n[23][24][25][26][27][28][29]'
startSat30 = '[  ][  ][  ][  ][  ][  ][ 1]\n[ 2][ 3][ 4][ 5][ 6][ 7][ 8]\n[ 9][10][11][12][13][14][15]\n[16][17][18][19][20][21][22]\n[23][24][25][26][27][28][29]\n[30][  ][  ][  ][  ][  ][  ]'
startSat31 = '[  ][  ][  ][  ][  ][  ][ 1]\n[ 2][ 3][ 4][ 5][ 6][ 7][ 8]\n[ 9][10][11][12][13][14][15]\n[16][17][18][19][20][21][22]\n[23][24][25][26][27][28][29]\n[30][31][  ][  ][  ][  ][  ]'







if month == monthList[0]:
    print(headJan)
    print(' Su   M   T   W   Th  F   S ')
    if value == 1:
        print(startSun31)
    elif value == 2:
        print(startMon31)
    elif value == 3:
        print(startTue31)
    elif value == 4:
        print(startWed31)
    elif value == 5:
        print(startThu31)
    elif value == 6:
        print(startFri31)
    elif value == 0:
        print(startSat31)
        
elif month == monthList[1]:
    print(headFeb)
    print(' Su   M   T   W   Th  F   S ')
    if (year%4) == 0:
        if value == 1:
            print(startSun29)
        elif value == 2:
            print(startMon29)
        elif value == 3:
            print(startTue29)
        elif value == 4:
            print(startWed29)
        elif value == 5:
            print(startThu29)
        elif value == 6:
            print(startFri29)
        elif value == 0:
            print(startSat29)
    elif (year%4) != 0:
        if value == 1:
            print(startSun28)
        elif value == 2:
            print(startMon28)
        elif value == 3:
            print(startTue28)
        elif value == 4:
            print(startWed28)
        elif value == 5:
            print(startThu28)
        elif value == 6:
            print(startFri28)
        elif value == 0:
            print(startSat28)
            
elif month == monthList[2]:
    print(headMar)
    print(' Su   M   T   W   Th  F   S ')
    if value == 1:
        print(startSun31)
    elif value == 2:
        print(startMon31)
    elif value == 3:
        print(startTue31)
    elif value == 4:
        print(startWed31)
    elif value == 5:
        print(startThu31)
    elif value == 6:
        print(startFri31)
    elif value == 0:
        print(startSat31)
        
elif month == monthList[3]:
    print(headApr)
    print(' Su   M   T   W   Th  F   S ')
    if value == 1:
        print(startSun30)
    elif value == 2:
        print(startMon30)
    elif value == 3:
        print(startTue30)
    elif value == 4:
        print(startWed30)
    elif value == 5:
        print(startThu30)
    elif value == 6:
        print(startFri30)
    elif value == 0:
        print(startSat30)
        
elif month == monthList[4]:
    print(headMay)
    print(' Su   M   T   W   Th  F   S ')
    if value == 1:
        print(startSun31)
    elif value == 2:
        print(startMon31)
    elif value == 3:
        print(startTue31)
    elif value == 4:
        print(startWed31)
    elif value == 5:
        print(startThu31)
    elif value == 6:
        print(startFri31)
    elif value == 0:
        print(startSat31)
        
elif month == monthList[5]:
    print(headJun)
    print(' Su   M   T   W   Th  F   S ')
    if value == 1:
        print(startSun30)
    elif value == 2:
        print(startMon30)
    elif value == 3:
        print(startTue30)
    elif value == 4:
        print(startWed30)
    elif value == 5:
        print(startThu30)
    elif value == 6:
        print(startFri30)
    elif value == 0:
        print(startSat30)
        
elif month == monthList[6]:
    print(headJul)
    print(' Su   M   T   W   Th  F   S ')
    if value == 1:
        print(startSun31)
    elif value == 2:
        print(startMon31)
    elif value == 3:
        print(startTue31)
    elif value == 4:
        print(startWed31)
    elif value == 5:
        print(startThu31)
    elif value == 6:
        print(startFri31)
    elif value == 0:
        print(startSat31)
        
elif month == monthList[7]:
    print(headAug)
    print(' Su   M   T   W   Th  F   S ')
    if value == 1:
        print(startSun31)
    elif value == 2:
        print(startMon31)
    elif value == 3:
        print(startTue31)
    elif value == 4:
        print(startWed31)
    elif value == 5:
        print(startThu31)
    elif value == 6:
        print(startFri31)
    elif value == 0:
        print(startSat31)
        
elif month == monthList[8]:
    print(headSep)
    print(' Su   M   T   W   Th  F   S ')
    if value == 1:
        print(startSun30)
    elif value == 2:
        print(startMon30)
    elif value == 3:
        print(startTue30)
    elif value == 4:
        print(startWed30)
    elif value == 5:
        print(startThu30)
    elif value == 6:
        print(startFri30)
    elif value == 0:
        print(startSat30)
        
elif month == monthList[9]:
    print(headOct)
    print(' Su   M   T   W   Th  F   S ')
    if value == 1:
        print(startSun31)
    elif value == 2:
        print(startMon31)
    elif value == 3:
        print(startTue31)
    elif value == 4:
        print(startWed31)
    elif value == 5:
        print(startThu31)
    elif value == 6:
        print(startFri31)
    elif value == 0:
        print(startSat31)

elif month == monthList[10]:
    print(headNov)
    print(' Su   M   T   W   Th  F   S ')
    if value == 1:
        print(startSun30)
    elif value == 2:
        print(startMon30)
    elif value == 3:
        print(startTue30)
    elif value == 4:
        print(startWed30)
    elif value == 5:
        print(startThu30)
    elif value == 6:
        print(startFri30)
    elif value == 0:
        print(startSat30)

elif month == monthList[11]:
    print(headDec)
    print(' Su   M   T   W   Th  F   S ')
    if value == 1:
        print(startSun31)
    elif value == 2:
        print(startMon31)
    elif value == 3:
        print(startTue31)
    elif value == 4:
        print(startWed31)
    elif value == 5:
        print(startThu31)
    elif value == 6:
        print(startFri31)
    elif value == 0:
        print(startSat31)