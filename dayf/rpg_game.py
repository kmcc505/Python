
# In this simple RPG game, Anakin Skywalker, finds out Chancellor Palpatine is a Sith Lord. 
# Skywalker goes into Palpatine's office alone. After all, he's the Chosen One. Why would he need anyone else?
# Entering Palpatine's office, he has three options:
    # 1. Fight Palpatine
    # 2. Do Nothing - in which case the Sith Lord will attack him anyway
    # 3. Pledge allegiance to Palpatine and the New Galactic Empire
    
from players import Player
from testmod import anakin_attack, emporer_attack

anakin = Player(10,5)
emporer = Player(6,7)

def main():

    while emporer.health > 0 and anakin.health > 0:
        print("You have {} health and {} power.".format(anakin.health, anakin.power))
        print("The emporer has {} health and {} power.".format(emporer.health, emporer.power))
        print()
        print("What do you want to do?")
        print("1. Fight the emporer! I'm the Chosen One.")
        print("2. Do nothing. I like him.")
        print("3. Go find Mace Windu for some reason.")
        print("> ", end=' ')

        raw_input = input()

        if raw_input == "1":
            anakin_attack()
        
        elif raw_input == "2":
            pass
        
        elif raw_input == "3":
            print("You tell Windu, but he's kind of a dick about it. He leaves you alone to think about the possibility of losing your beloved Padme.")
            print("You rush into the fray just as Windu is defeating the emporer. You cut Windu's arm off and help Palpatine kill him.")
            print("Long story short, you become Darth Vader to save Padme but she dies anyway.")
            break
        
        else:
            print("Invalid input {}".format(raw_input))

        if emporer.health > 0:
            emporer_attack()

main() 