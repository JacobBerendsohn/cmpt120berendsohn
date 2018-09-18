# pi.py

def main():

    n = int(input("Input a number to iterate pi with: "))
    pi = 0
    sign = 1
    
    for i in range(1,2*(n+1),2):
        pi = pi+sign*(4/i)
        sign=sign*-1
        
    print("Pi is:", pi)

main()
    
