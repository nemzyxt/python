#Author : Nemuel Wainaina
#Program that takes a number as input from the user, calculates the factorial and prints it back to the user

def factorial(num):
    '''
    Function to calculate the factorial of a number
    '''
    if num <= 0:
        return 1
    else:
        return num * factorial(num - 1)
    
def main():
    while True:
        num = int(input("Enter the number : "))
        fact =  factorial(num)
        print(f"[+] The factorial of {num} is {fact}\n")
    
    
#call the main function
main()