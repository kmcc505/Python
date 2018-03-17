# write a function that prompts user for input to ask if they want to play again. return true if Y

def run():
    x = input('Do you want to play a game? Y or N? ')
    if x == 'Y':
        return True
    elif x == 'N':
        return False
    else:
        print('Invalid input')
        run()

if __name__ == "__main__":
    run()
