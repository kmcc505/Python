
def anakin_attack():
         # anakin attacks emporer
    emporer.health -= anakin.power
    print("You do {} damage to the emporer.".format(anakin.power))
    if emporer.health <= 0:
        print("YOU HAVE FULFILLED YOUR DESTINY AS THE CHOSEN ONE IN THE MOST EFFECTIVE AND EFFICIENT WAY POSSIBLE! YAY!!")

def emporer_attack():
         # emporer attacks anakin
    anakin.health -= emporer.power
    print("The emporer does {} damage to you.".format(emporer.power))
    if anakin.health <= 0:
        print("The emporer kills you. WTF.")