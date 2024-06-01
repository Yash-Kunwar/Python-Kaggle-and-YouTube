# Author : Orpheus :)
print("twinkle twinkle little star")

for i in range (1,11):
    print(5*i)

import os
cwd = os.getcwd() # Get the current working directory

files = os.listdir(cwd)# Get a list of all the files and directories in the current working directory

for file in files: # Print the contents of the directory
    print(file)
