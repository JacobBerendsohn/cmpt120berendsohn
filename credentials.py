# CMPT 120 Intro to Programming
# Lab #5 – Working with Strings and Functions
# Author: Jacob Berendsohn
# Created: 2018-09-24


# Main function of the code
def main():
    name = getName()
    uname = buildUser(name[0], name[1])
    password = passMake()
    print("Account configured. Your new email address is",uname + "@marist.edu")


# Gets the first and last name into a list
def getName():
    name = []
    name.append(input("Enter your first name: "))
    name.append(input("Enter your last name: "))
    return name
        


# Builds a marist style username
def buildUser(fName, lName):
    uname = fName + (".") + lName + ("1")
    return uname.lower()
    
    

# Creates password
def passMake():
    # ask user to create a new password
    passwd = input("Create a new password: ")
    passTest(passwd)
    return passwd


# Tests password strength
def passTest(password):
    if (len(password) > 8 and password.lower() != password and password.upper() != password and any(char.isdigit() for char in password)):
        print("The force is strong in this one…")
    else:
        print("Fool of a Took! That password is feeble!")
        passMake()

main()

    





