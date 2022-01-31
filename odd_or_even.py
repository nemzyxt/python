#Author : Nemuel Wainaina
#Program to check whether a number is even or odd

def check_num(num):
    if num % 2 == 0:
        print(f"{num} is Even")
    else:
        print(f"{num} is Odd")
        
while True:
    num = int(input("Enter a number : "))
    check_num(num)