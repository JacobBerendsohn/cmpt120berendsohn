# CMPT 120 - Lab #6
# Jacob Berendsohn
# 16-10-2018
###
def showIntro():
    print("Welcome to the Arithmetic Engine!")
    print("=================================\n")
    print("Valid commands are 'add', 'mult', 'sub', 'div', and 'quit'.\n")


def showOutro():
    print("\nThank you for using the Arithmetic Engine…")
    print("\nPlease come back again soon!")

def doLoop():
    while True:
        cmd = input("What computation do you want to perform? ")
        cmd = cmd.lower()
        if(cmd == "add" or cmd == "sub" or cmd == "mult" or cmd == "div" or cmd == "quit"):
            try:
                num1 = int(input("Enter the first number: "))
                num2 = int(input("Enter the second number: "))
            except:
                print("Error: Enter valid inputs.")
                continue
            if cmd == "add":
                result = num1 + num2
            elif cmd == "sub":
                result = num1 - num2
            elif cmd == "mult":
                result = num1 * num2
            elif cmd == "div":
                result = num1 // num2
            elif cmd == "quit":
                break
        else:
            print(cmd, "is not a valid input.")
            break
        print("The result is " + str(result) + ".\n")

def main():
    showIntro()
    doLoop()
    showOutro()

main()
