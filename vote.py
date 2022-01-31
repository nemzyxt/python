#Author : Nemuel Wainaina
#Program takes age as input from the user and tells the user whether or not they are eligible to vote

while True:
    age = int(input("Please enter your age : "))
    if age < 18:
        print("[!] You cannot vote . Too young !")
    else:
        print("[+] You can vote ")
    print()