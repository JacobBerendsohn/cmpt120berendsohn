# fibonacci.py
# Gives a fibonacci sequence with a starting number

def main():
    
    startNum = int(input("Please enter Nth number you would like to find in the fibonacci sequence: "))

    F  = 0
    F0 = 0
    F1 = 1
    
    for i in range(startNum):
        if i == startNum-1:
            print("The Nth number is:",F1)
        F = F0
        F0 = F1
        F1 = F + F0

main()

        
    
    
    
