#secret number game where user guesses between 1 and 10 
import random #imports random module for random number generation
secret_num = random.randint(1,10) #generates random in in range 1-10

guess = input("I'm thinking of a number between 1 and 10. Guess!!! " ) #asks user for input
guess_num = 5 #This is the number of guesses the user has to get the answer right

while int(guess) != int(secret_num): #loops runs while the user's guess does not equal the random secret number.
    guess_num = guess_num - 1 #takes a guess away for each loop

    if int(guess) > int(secret_num): #here's what happens if the guess is too high
        guess = input("Too high. Try again! ")
        print("You have " + str(guess_num)+ " guesses left.")

    elif int(guess) < int(secret_num): #here's what happens if the guess is too low
        guess = input("Too low. Try again! ")
        print("You have " + str(guess_num)+ " guesses left.")

print("Congrats! You win!") #displays only when user's guess is == random secret number
