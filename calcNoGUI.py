# calcNoGUI.py
# Creating a calculator without the use of a graphical user interface

def main():
    # Makes a list to hold the equation
    equation = []
    equation = (input("Please enter a basic calculation with no spaces: "))
    # Gets list length for the for loop
    eqLen = len(equation)

# Does main calculations for the calulator
def calc():
    for i in range(eqLen):
        if(i=="*" || i=="/"):
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
