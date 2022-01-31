#Author : Nemuel Wainaina
#Command Prompt in Python

import os
import subprocess

while True:
    cur_dir = os.getcwd()
    cmd = input(f"{cur_dir}# ")
    result = subprocess.getoutput(cmd)
    print(result + "\n")
    