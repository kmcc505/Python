#prompts user for file name then prints letter histogram of contents
file_read = open(input('name of file? '), 'r')
contents = file_read.read()
file_read.close()

counts = {}
for x in contents:
    if x not in counts:
        counts[x]=1
    else:
        counts[x]+=1
print(counts)