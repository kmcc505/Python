#Coin game: If user says yes, add total. If no, say bye
answer = input('Would you like another coin? Type yes or no: ')#asks user for input as 'yes' or 'no'
answer = answer.lower() #converts all letters to lowercase
count = 0 #baseline count

while answer == "yes": #Loop start
    count = count + 1  #This adds one to the count each loop
    print('You have this many coins: ' + str(count))  #This prints the statement of how many coins the user has to the console.
    answer = input('Would you like another coin? Type yes or no: ') 
    answer = answer.lower()
print ('Well...bye')   #end of game 