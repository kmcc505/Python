#prompt user for name, say hello in upper case and tell how many letters in name
name = input('What is your name? ')
upper_name = name.upper()
len_name = len(upper_name)
str_name = str(len_name)
print('HELLO ' + upper_name + '!')
print("YOUR NAME HAS " + str_name + " LETTERS IN IT. AWESOME, BRUH!")
