# calcNoGUI.py
# Creating a calculator without the use of a graphical user interface

def main():
    # Makes a list to hold the equation
    equation = []
    equation = (input("Please enter a basic calculation with spaces between everything: "))
    # Gets list length for the for loop
    equation.split()
    eqLen = len(equation)
    final = calc(eqLen, equation)
    print("Your answer is:",final)

# Does main calculations for the calulator
def calc(listLength, equation = []):
    eqLen = listLength
    # If statement to check if problem has been solved
    if(eqLen!=1):
        # For loop to loop through given equation
        for i in range(eqLen):
            # Beginning PEMDAS by checking for * or /
            if((equation[i]=="*") or (equation[i]=="/")):
                if(equation[i]=="*"):
                    product = mult(int(equation[i-2]), int(equation[i+2]))
                    product = str(product)
                    del equation[0]
                    del equation[4]
                elif(equation[i]=="/"):
                    quotient = div(int(equation[i-1]), int(equation[i+1]))
                    quotient = str(quotient)
                    equation.replace(equation[i-1], quotient)
                    equation.remove(int(equation[i]))
                    equation.remove(int(equation[i+1]))
            # Next step in PEMDAS by checking for + or -
            elif((equation[i]=="+") or (equation[i]=="-")):
                if(equation[i]=="+"):
                    numSum = add(int(equation[i-1]), int(equation[i+1]))
                    numSum = str(numSum)
                    equation.replace(equation[i-1], numSum)
                    equation.remove(str(equation[i]))
                    equation.remove(str(equation[i+1]))
                elif(equation[i]=="-"):
                    difference = sub(int(equation[i-1]), int(equation[i+1]))
                    difference = str(difference)
                    equation.replace(equation[i-1], difference)
                    equation.remove(str(equation[i]))
                    equation.remove(str(equation[i+1]))
            eqLen = len(equation)
    else:
        return finalAnswer

# Multiplication Function
def mult(num1, num2):
    answer = num1*num2
    return answer

# Division Function
def div(num1, num2):
    answer = num1/num2
    return answer

# Addition Function
def add(num1, num2):
    answer = num1+num2
    return answer

# Subtraction Function
def sub(num1, num2):
    answer = num1-num2
    return answer

main()
