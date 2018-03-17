# ask for day of week by number; if weekend, tell to 'sleep in'; if other say 'go to work'
day = int(input('Day (0-6)? '))
if day == 0 or 6:
    print("Sleep in")
else:
     print("Go to work")     
