#Author : Nemuel Wainaina
#Prints out the current date and time from the system

from datetime import datetime as dt

cur_date = dt.now().strftime("%x")
cur_time = dt.now().strftime("%X")
print(cur_date + " " + cur_time)