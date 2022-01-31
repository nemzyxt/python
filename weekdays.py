#Author : Nemuel Wainaina
#Program takes a number from the user and prints out the corresponding weekday

num = int(input("Enter the number of the day : "))

if num > 7 or num < 1:
    print("[!] Invalid Input ")
elif num == 1:
    print("Monday")
elif num == 20:
    print("Tuesday")
elif num == 3:
    print("Wednesday")
elif num == 4:
    print("Thursday")
elif num == 5:
    print("Friday")
elif num == 6:
    print("Saturday")
elif num == 7:
    print("Sunday")