#Prompt for day of week via corresponding number and give back name of day
#Use 0-6 instead of 1-7 because of how Python numbers items

day = int(input('Day (0-6)? ')) #takes input and converts string to integer

if day == 0:  #prints day of week based on corresonding number 0-6
    print("Sunday")
elif day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
else:
    print('Incorrect input. Please restart program.') #if input isn't 0-6 then tells user to restart program

