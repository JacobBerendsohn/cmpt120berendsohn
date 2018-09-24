# CMPT 120 Intro to Programming
# Lab #5 – Working with Strings and Functions
# Author: Jacob Berendsohn
# Created: 2018-09-24


# Gets the first and last name into a list
def getName():

    name = []
    name.append(input("Enter your first name: "))
    name.append(input("Enter your last name: "))

    return name
        


# Builds a marist style username
def buildUser(fName, lName):

    uname = fName + (".") + lName + ("1")

    return uname
    
    

# Checks password strength
def passTest():

    # ask user to create a new password
    passwd = input("Create a new password: ")
    
    while len(passwd) < 8:
        print("Fool of a Took! That password is feeble!")
        passwd = input("Create a new password: ")

    print("The force is strong in this one…")

    return passwd



# Main function of the code
def main():

    name = getName()
    uname = buildUser(name[0], name[1])
    passTest()
    
    print("Account configured. Your new email address is",uname + "@marist.edu")

main()
    





