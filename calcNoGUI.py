# calcNoGUI.py
# Creating a calculator without the use of a graphical user interface

def main():
    # Makes a list to hold the equation
    equation = (list(input("Please enter a basic calculation with spaces between everything: ")))
    # Gets list length for the for loop
    eqLen = len(equation)
    final = calc(eqLen, equation)
    print("Your answer is:",final)

# Does main calculations for the calulator
def calc(listLength, equation = []):
    eqLen = listLength
    # For loop to loop through given equation
    for i in range(int(eqLen/2)+1):
        # Beginning PEMDAS by checking for * or /
        if((equation[i]=="*") or (equation[i]=="/")):
            if(equation[i]=="*"):
                product = mult(int(equation[i-1]), int(equation[i+1]))
                newProduct = str(product)
                equation1 = equation
                equation = []
                equation.append(newProduct)
                if(len(equation1) < 3):
                    for index in range(len(equation1)):
                        equation.append(equation1[index+2])
                equation1 = []
                print(equation)
            elif(equation[i]=="/"):
                quotient = div(int(equation[i-1]), int(equation[i+1]))
                newQuotient = str(quotient)
                equation1 = equation
                equation = []
                equation.append(newQuotient)
                if(len(equation1) < 3):
                    for index in range(len(equation1)):
                        equation.append(equation1[index+2])
                equation1 = []
                print(equation)
        # Next step in PEMDAS by checking for + or -
        elif((equation[i]=="+") or (equation[i]=="-")):
            if(equation[i]=="+"):
                numSum = add(int(equation[i-1]), int(equation[i+1]))
                newNumSum = str(numSum)
                equation1 = equation
                equation = []
                equation.append(newNumSum)
                if(len(equation1) < 3):
                    for index in range(len(equation1)):
                        equation.append(equation1[index+2])
                equation1 = []
                print(equation)
            elif(equation[i]=="-"):
                difference = sub(int(equation[i-1]), int(equation[i+1]))
                newDifference = str(difference)
                equation1 = equation
                equation = []
                equation.append(newDifference)
                if(len(equation1) < 3):
                    for index in range(len(equation1)):
                        equation.append(equation1[index+2])
                equation1 = []
                print(equation)
                
    finalAnswer = equation[0]
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
