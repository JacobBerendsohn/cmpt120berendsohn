# guessing-game.py
# A game where the usre must guess an animal

def main():
    wrong = True
    while(wrong):
        animal = "octopus"
        print("I am thinking of an animal")
        guess = input("Guess the animal I am thinking of: ")
        if(guess.lower() == animal):
            wrong = False
        else:
            print("Incorrect try again :(")
    print("YOU GOT THE RIGHT ANIMAL")
main()
    
