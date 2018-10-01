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

print('After year/4', value)

#Century Value Calulations
if century_digits == 18:
    value = value + 2
elif century_digits == 20:
    value = value + 6

print('After cent calc', value)

#Month Value Calculations
while month == None:
    if month == 'Jan' and (year%4 != 0):
        value=+1
        break
    elif month == 'Feb' and (year%4 == 0):
        value=+3
        break
        if month == 'Feb' and (year%4 != 0):
         value=+4
         break
    elif month == 'Mar' or 'Nov':
        value=+4
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

        
print('After month calc', value)

value = value + day
print('After day calc', value)
total = value%7

print ('Total', total)
if total == 1:
    print('The day is Sunday')
elif total == 2:
    print('The day is Monday')
elif total == 3:
    print('The day is Tuesday')
elif total == 4:
    print('The day is Wednesday')
elif total == 5:
    print('The day is Thursday')
elif total == 6:
    print('The day is Friday')
elif total == 0:
    print('The day is Saturday')


