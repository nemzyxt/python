#Author : Nemuel Wainaina
#Program to print all the prime number from 1 to 100

def is_prime(num):
    factors = 0
    for i in range(1, num + 1):
        if num % i == 0:
            factors += 1
    if factors == 2:
        return True
    else:
        return False
    
count = 0
for i in range(1, 101):
    if is_prime(i):
        count += 1
        print(f"{i} is a prime number")
print(f"[+] There are {count} Prime Numbers between 1 and 100")