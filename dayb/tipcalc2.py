#same as tipcalc.py but splits total per person entered via input
bill = (float(input('What is the bill amount? ')))
service = input('Was the service good, fair or bad? ')
split = (float(input('Bill split how many ways tho? ')))
if service == 'good':
    tip = bill * .20
    total = bill * 1.20
if service == 'fair':
    tip = bill * .15
    total = bill * 1.15
if service == 'bad':
    tip = bill * .10
    total = bill * 1.10

print('Tip Amount: $' + '{:.2f}'.format(tip)) 
print('Total Bill: $' + '{:.2f}'.format(total)) 
print('Per Person: $' + '{:.2f}'.format(total/split)) 