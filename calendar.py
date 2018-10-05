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
elif month == monthList[2] or monthList[10]:
    value= value +4
elif month == monthList[3] or monthList[6]:
    value= value +0
elif month == monthList[4]:
    value= value +2
elif month == monthList[5]:
    value= value +5
elif month == monthList[7]:
    value= value +3
elif month == monthList[9]:
    value= value +1
elif month == monthList[8] or monthList[11]:
    value= value +6
  


day = 0
#Days in month
if month == monthList[1]:
    if (year%4)==0:
        day = 29
        print('I got here')
    else:
        day = 28
        print('I am this one')
elif month in('Jan', 'Mar', 'May', 'Jul', 'Aug', 'Oct', 'Dec'):
    day = 31
    print('31 days!')
elif month in('Sep', 'Apr', 'Jun', 'Nov'):
    day = 30
    print('30 days!')

    

value = (value + 1)%7



if value == 1:
    print('The day is Sunday')
elif value == 2:
    print('The day is Monday')
elif value == 3:
    print('The day is Tuesday')
elif value == 4:
    print('The day is Wednesday')
elif value == 5:
    print('The day is Thursday')
elif value == 6:
    print('The day is Friday')
elif value == 0:
    print('The day is Saturday')





#Format!


headJan = print(format('-', '-<10'), 'January', format('-', '-<10'))

headFeb = print(format('-', '-<10'), 'February', format('-', '-<10'))

headMar = print(format('-', '-<10'), 'March', format('-', '-<10'))

headApr = print(format('-', '-<10'), 'April', format('-', '-<10'))

headMay = print(format('-', '-<10'), 'May', format('-', '-<10'))

headJun = print(format('-', '-<10'), 'June', format('-', '-<10'))

headJul = print(format('-', '-<10'), 'July', format('-', '-<10'))

headAug = print(format('-', '-<10'), 'August', format('-', '-<10'))

headSep = print(format('-', '-<10'), 'September', format('-', '-<10'))

headOct = print(format('-', '-<10'), 'October', format('-', '-<10'))

headNov = print(format('-', '-<10'), 'November', format('-', '-<10'))

headDec = print(format('-', '-<10'), 'December', format('-', '-<10'))


startSun = '[1][2][3][4][5][6][7]'
startMon = '[][1][2][3][4][5][6]'
startTue = '[][][1][2][3][4][5]'
startWed = '[][][][1][2][3][4]'
startThu = '[][][][][1][2][3]'
startFri = '[][][][][][1][2]'
startSat = '[][][][][][][1]'





print(headJan)
print(startSun)










