#Author : Nemuel Wainaina
#Program checks whether a number is positive or negative

def check_num(num):
    if num > 0:
        print(f"{num} is Positive")
    elif num < 0:
        print(f"{num} is Negative")
    else:
        print("The number is 0")
    
while True:
    num = int(input("Enter a number : "))
    check_num(num)