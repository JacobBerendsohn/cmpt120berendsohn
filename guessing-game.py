# guessing-game.py
# A game where the usre must guess an animal

def main():
    
    wrong = True
    
    while(wrong):
        print("I am thinking of an animal")
        animal = "octopus"
        guess = input("Guess the animal I am thinking of: ")
        
<<<<<<< HEAD
        if(guess.lower() == "quit"):
=======
        if(guess[0].lower() == "q"):
>>>>>>> GuessingImprovements
            wrong = False
        elif(guess.lower() == animal.lower()):
            print("YOU GOT THE RIGHT ANIMAL")
            like = input("Do you like this animal? (y or n) ")
            wrong = False
        else:
            print("Incorrect try again :(")
main()
    
