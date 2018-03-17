#promt user for file name, read file and print to screen
file_read = open(input('name of file?'), 'r')
contents = file_read.read()
file_read.close()

print(contents)

