#Asks user for bill info and printstip amout and bill total based on service level
bill = (float(input('What is the bill amount? ')))
service = input('Was the service good, fair or bad? ')
if service == 'good':
    tip = bill * .20
    total = bill * 1.20
elif service == 'fair':
    tip = bill * .15
    total = bill * 1.15
elif service == 'bad':
    tip = bill * .10
    total = bill * 1.10

print("Tip Amount: $" + "{:.2f}".format(tip)) 
print("Total Bill: $" + "{:.2f}".format(total))     
