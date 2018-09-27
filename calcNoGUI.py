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
    # For loop to loop through given equation
    for i in range(eqLen):
        # Beginning PEMDAS by checking for * or /
        if((equation[i]=="*") or (equation[i]=="/")):
            if(equation[i]=="*"):
                product = mult(int(equation[i-2]), int(equation[i+2]))
                newProduct = str(product)
                equation.replace(equation[i+2], newProduct)
                equation.replace(equation[i-2], "")
                equation.replace(equation[i], "")
                print(equation)
            elif(equation[i]=="/"):
                quotient = div(int(equation[i-2]), int(equation[i+2]))
                newQuotient = str(quotient)
                equation.replace(equation[i+2], newQuotient)
                equation.replace(equation[i-2], "")
                equation.replace(equation[i], "")
                print(equation)
        # Next step in PEMDAS by checking for + or -
        elif((equation[i]=="+") or (equation[i]=="-")):
            if(equation[i]=="+"):
                numSum = add(int(equation[i-2]), int(equation[i+2]))
                newNumSum = str(numSum)
                equation.replace(equation[i+2], newNumSum)
                equation.replace(equation[i-2], "")
                equation.replace(equation[i], "")
                print(equation)
            elif(equation[i]=="-"):
                difference = sub(int(equation[i-2]), int(equation[i+2]))
                newDifference = str(difference)
                equation.replace(equation[i+2], newDifference)
                equation.replace(equation[i-2], "")
                equation.replace(equation[i], "")
                print(equation)
                
    finalAnswer = equation[eqLen-1]
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
