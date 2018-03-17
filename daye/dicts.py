#This is a dictionary phone book
phonebook = {
    'Alice': '703-493-1834',
    'Bob':'857-384-1234',
    'Elizabeth':'484-584-2923'
}
#Print Elizabeth's number
print(phonebook['Elizabeth'])

#Add entry for Kareem's number
phonebook['Kareem']='938-489-1234'

#Delete Alice entry
del phonebook['Alice']
print(phonebook['Kareem'])

#Change Bob's number
phonebook['Bob']='968-345-2345'

#Print phonebook 
for key, value in phonebook.items():
    print (key, ':',value)
    
