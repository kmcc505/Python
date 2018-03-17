#Various exercises with Python lists

#Sums the numbers in a mylist
mylist = [4,8,15,16,23,42]
numsum = sum(mylist)
print(numsum)

#prints largest number in a list
highest = max(mylist)
print(highest)

#prints lowest number in a list
lowest = min(mylist)
print(lowest)

#prints even and odd numbers in list into separate lists
even_numbers = []
odd_numbers = []
for number in [4,8,15,23,42]:
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)
print (even_numbers)
print(odd_numbers)

#prints positive numbers in a new list and negative numbers to separate list
pos_numbers = []
neg_numbers = []
for number in [4,8,15,-23,42]:
    if number > 0:
        pos_numbers.append(number)
    else:
        neg_numbers.append(number)
print (pos_numbers)
print (neg_numbers)

#Multiplies a list of numbers by a single factor
myotherlist = [2, 4, 6, 8]
result = []
for num in myotherlist:
    result.append(num * 2)
print(result)

#Multiplies vectors
even  = [2,4,6]
odd = [1,3,5]
x = (even[0] * odd[0])
y = (even[1] * odd[1])
z = (even[2] * odd[2])
vectors = [x, y, z]
print(vectors)

#Removes duplicate values via set
dupelist = [2, 2, 2, 4, 6, 10, 206]
new = set(dupelist)
print(new)
