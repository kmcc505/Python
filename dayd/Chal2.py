# Find sum of multiples of 3 and 5 from 1-1000
newlist = []
for i in range(1,1000):
    if (i % 3 == 0) or (i % 5 == 0):
        newlist.append(i)
print(sum(newlist))

