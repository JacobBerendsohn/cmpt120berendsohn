# calc_functions.py
# Creating a calculator without the use of a GUI, can solve with the 4 basic operators, and no parenthesis

def main():
    # Makes a list to hold the equation
    eq = (list(input("Please enter a basic calculation without spaces: ")))
    
    # Fixed the input in the list to have numbers with more than one digit
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
        
        # Checks for the operators in the equation to know where the numbers are in relation to operators
        if(oldEq[n] == "+" or oldEq[n] == "-" or oldEq[n] == "*" or oldEq[n] == "/"):
            
            number = oldEq[n-i: n]
            newNumber = "".join(number)
            finEq.append(newNumber)
            finEq.append(oldEq[n])
            i = 0
            number = ""
            
        # This elif is for the last item in the list
        elif(len(oldEq) == n+1):
            number = oldEq[n-i: n+1]
            newNumber = "".join(number)
            finEq.append(newNumber)
            i = 0
            number = ""

        # This is the counter to know how many numbers there are before the operator
        else:
            i = i+1

    # Returns final concatentated equation to give to calculator function
    return finEq

# Does main calculations for the calulator
def calc(equation = []):
    
    # For loop to loop through given equation, and to close when one index remains
    while(len(equation) != 1):

        # Making sure pemdas works for multiple division and multiplication operators in same equation
        while(("*" in equation) or ("/" in equation)):
            
            for i in range(1, len(equation)):
                
                # Beginning PEMDAS by checking for * or /
                if((equation[i]=="*") or (equation[i]=="/")):

                    # Multiplication
                    if(equation[i]=="*"):
                        
                        product = mult(float(equation[i-1]), float(equation[i+1]))
                        product = str(product)
                        equation = ins(product, i, equation)
                        break

                    # Division
                    elif(equation[i]=="/"):
                        
                        quotient = div(float(equation[i-1]), float(equation[i+1]))
                        quotient = str(quotient)
                        equation = ins(quotient, i, equation)
                        break
                    break

        # Next step in PEMDAS by checking for + or -
        for i in range(1, len(equation)):
            
            if((equation[i]=="+") or (equation[i]=="-")):

                # Addition
                if(equation[i]=="+"):
                    
                    numSum = add(float(equation[i-1]), float(equation[i+1]))
                    numSum = str(numSum)
                    equation = ins(numSum, i, equation)
                    break

                # Subtraction
                elif(equation[i]=="-"):
                    
                    difference = sub(float(equation[i-1]), float(equation[i+1]))
                    difference = str(difference)
                    equation = ins(difference, i, equation)
                    break
                
                break
        
    finalAnswer = equation[0]

    # Returns final answer
    return finalAnswer

# Completes the insertion of the new term and deletion of the old
def ins(finalNum, i, equation = []):
    del equation[i-1:i+2]
    equation.insert(i-1, finalNum)
    print(equation)
    return equation

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
