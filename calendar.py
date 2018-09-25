#Noah Smith Gunnar Nick
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

import math

#greeting -
print('Hey there and welcome to the calendar program!')


#var list

year = int(input('What year are you looking for. 1800-2099'))

century_digits = int(str(year)[:2])

year_digits = int(str(year)[-2:])

month = input('Please input a month. ex: Jan, Feb, Mar')

day = int(input('What day fool?'))

value = year_digits + math.floor(year_digits/4)


#Century Value Calulations
if century_digits == 18:
    value = value + 2
elif century_digits == 20:
    value = value + 6

#Month Value Calculations
while True:
    if month == 'Jan' and year%4 != 0:
        value = value + 1
        if year%4 == 0:
            value = value + 3
            break
    elif month == 'Feb' and year%4 == 0:
        value = value + 3
        if year%4 != 0:
            value = value + 4
            break
    elif month == 'Mar' or 'Nov':
        value = value + 4
        break
    elif month == 'Apr' or 'Jul':
        value = value + 0
        break
    elif month == 'May':
        value = value + 2
        break
    elif month == 'Jun':
        value = value + 5
        break
    elif month == 'Aug':
        value = value + 3
        break
    elif month == 'Oct':
        value = value + 1
        break
    elif month == 'Sep' or 'Dec':
        value = value + 6
        break
    else:
        print('Why did you not give me a correct answer? I thought I was clear enough.')
    
value = (value + day)%7

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

