#Various exercies with Python loops

# print numbers between 1 and 10
for number in range (1, 10):
    print(number)

#same as above with prompt of start and end
startfrom = input('Start from: ')
endon = input('End on: ')
x = int(startfrom)
y = int(endon)
for number in range (x,y):
    print(number)

#print each odd number between 1 and 10 inclusive
odd_numbers = []
for number in range (1, 10):
    if number % 2 != 0:
        print(number)

#print a 5 by 5 sqare of * characters
x = '*****'
count = 0
while count < 5:
    print(x)
    count = count + 1
  
#print a ___ by ___ square of *; ask user for ___
userinput = input('Enter a value: ')
count = 0
y = '*'
userinput = int(userinput)
display = userinput * y
while count < userinput:
    print(display)
    count = count + 1

#print a box and ask user for h and w
height = int(input('Enter height: '))
width = int(input('Enter width: '))
count = 0
y = '*'
while count < height:
    if count == 0:
        print(y * height)
    if count != 0 or count != height-1:
        print (y + (' ' * width + y))
    if count == height-1:
        print(y * height)
    count = count + 1

#print a triangle
height = 10
for i in range (height, 0, -1):
    print (i * ' ' + (height + 1 - i) * '*')



   