#Nested dictionary exercices

ramit = {
  'name': 'Ramit',
  'email': 'ramit@gmail.com',
  'interests': ['movies', 'tennis'],
  'friends': [
    {
      'name': 'Jasmine',
      'email': 'jasmine@yahoo.com',
      'interests': ['photography', 'tennis']
    },
    {
      'name': 'Jan',
      'email': 'jan@hotmail.com',
      'interests': ['movies', 'tv']
    }
  ]
}
#python expression that gets email addy of Ramit
addy = ramit.get('email',)
print(addy)

#python expression that gets first of Ramit's interest
print(ramit.get('interests')[0])


#gets email addy of Jasmine
print(ramit.get('friends')[0]['email'])

#get for second of Jan's interest
print(ramit.get('friends')[1]['interests'][1])

#letter histogram counts for 'banana'
word = 'banana'
counts = {}
for char in word:
    if char not in counts:
        counts[char]=1
    else:
        counts[char]+=1
print(counts)