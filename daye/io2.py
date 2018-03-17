#prompt for file name, promt to write content to file, then saves content
file_write = open(input('name of file?'), 'w')
content = file_write.write(input('enter content here '))
file_write.close()


