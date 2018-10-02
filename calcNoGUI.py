# calcNoGUI.py
# Creating a calculator without the use of a graphical user interface

def main():
    # Makes a list to hold the equation
    eq = (list(input("Please enter a basic calculation with spaces between everything: ")))
    # Gets list length for the for loop
    equation = concat(eq)
    print(equation)
    final = calc(equation)
    print("Your answer is:",final)

# Makes the list hold numbers with more than one digit
def concat(oldEq = []):
    finEq = []
    i = 0
    number = ""
    for n in range(len(oldEq)):
        if(oldEq[n] == "+" or oldEq[n] == "-" or oldEq[n] == "*" or oldEq[n] == "/"):
            number = oldEq[n-i: n]
            newNumber = "".join(number)
            finEq.append(newNumber)
            finEq.append(oldEq[n])
            i = 0
            number = ""
        elif(len(oldEq) == n+1):
            number = oldEq[n-i: n+1]
            print(number)
            newNumber = "".join(number)
            finEq.append(newNumber)
            i = 0
            number = ""
        else:
            i = i+1
    return finEq

# Does main calculations for the calulator
def calc(equation = []):
    for num in range(eqLen):
    # For loop to loop through given equation
    while(len(equation) != 1):
        for i in range(1, len(equation)):
            # Beginning PEMDAS by checking for * or /
            if((equation[i]=="*") or (equation[i]=="/")):
                if(equation[i]=="*"):
                    product = mult(int(equation[i-1]), int(equation[i+1]))
                    del equation[i-1:1+2]
                    equation.insert[i-1, product]
                    print(equation)
                elif(equation[i]=="/"):
                    quotient = div(int(equation[i-1]), int(equation[i+1]))
                    
                    print(equation)
            # Next step in PEMDAS by checking for + or -
            elif((equation[i]=="+") or (equation[i]=="-")):
                if(equation[i]=="+"):
                    numSum = add(int(equation[i-1]), int(equation[i+1]))
                    
                    print(equation)
                elif(equation[i]=="-"):
                    difference = sub(int(equation[i-1]), int(equation[i+1]))
                    
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
