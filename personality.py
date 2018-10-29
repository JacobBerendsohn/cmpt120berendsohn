# Get the mode of interaction from the user
# Params: none
# Returns: an integer indicating one of reward, punish, joke, or threaten
def main():
    currEmotion = 3
    while(True):
        currAction = getInteraction()
        newEmotion = lookupEmotion(currEmotion, currAction)
        currEmotion = showEmotion(newEmotion)

def getInteraction():
    # TODO prompt user to choose an action

    print("What would you like to do to the AI?")
    print("1: Reward")
    print("2: Punish")
    print("3: Threaten")
    print("4: Joke")
    currAction = int(input("Choose: "))
    currAction = (currAction - 1)
    return currAction # return a corresponding integer
    
# Based on a given emotion and action, determine the next emotional state
# Params:
# currEmotion - a current emotion
# userAction - a user interaction
# Returns: an emotion

def lookupEmotion(currEmotion, userAction):
    # Rows are emotions, starting from row 0 they are
    # Anger, disgust, fear, happiness, sadness, surprise
    # Columns are actions, starting from column 0 they are
    # Reward, punish, threaten, joke
    responses = [[5, 4, 2, 1],
                 [3, 0, 0, 1],
                 [5, 4, 2, 3],
                 [5, 1, 4, 3],
                 [1, 0, 2, 3],
                 [5, 0, 1, 3]]
    # TODO do the matrix lookup
    newEmotion = responses[currEmotion][userAction]
    return newEmotion # return an integer corresponding to an emotion

def showEmotion(newEmotion):
    if(newEmotion == 0):
        print("You're making me angry...")
        print("")
        return(0)
    elif(newEmotion == 1):
        print("Ewwwww, I can't believe you!")
        print("")
        return(1)
    elif(newEmotion == 2):
        print("Stop you're scaring me :(")
        print("")
        return(2)
    elif(newEmotion == 3):
        print("That makes me happy :)")
        print("")
        return(3)
    elif(newEmotion == 4):
        print("I'm going to cry...")
        print("")
        return(4)
    else:
        print("WOW that was unexpected.")
        print("")
        return(5)
main()
