# calcNoGUI.py
# Creating a calculator without the use of a graphical user interface

def main():
    # Makes a list to hold the equation
    equation = []
    equation = (input("Please enter a basic calculation with no spaces: "))
    # Gets list length for the for loop
    eqLen = len(equation)
    final = calc():
    print("Your answer is:",final)

# Does main calculations for the calulator
def calc():
    # If statement to check if problem has been solved
    if(eqLen!=1):
        # For loop to loop through given equation
        for i in range(eqLen):
            # Beginning PEMDAS by checking for * or /
            if((i=="*") or (i=="/")):
                if(i=="*"):
                    product = mult(equation[i-1], equation[i+1])
                    equation[i] = product
                    equation.remove(i-1)
                    equation.remove(i+1)
                elif(i=="/"):
                    quotient = div(equation[i-1], equation[i+1])
                    equation[i] = quotient
                    equation.remove(i-1)
                    equation.remove(i+1)
            # Next step in PEMDAS by checking for + or -
            elif((i=="+") or (i=="-")):
                if(i=="+"):
                    numSum = add(equation[i-1], equation[i+1])
                    equation[i] = numSum
                    equation.remove(i-1)
                    equation.remove(i+1)
                if(i=="-"):
                    difference = sub(equation[i-1], equation[i+1])
                    equation[i] = difference
                    equation.remove(i-1)
                    equation.remove(i+1)
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
