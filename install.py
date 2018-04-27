#!/usr/bin/python3
from time import sleep
import os

print('''
Select operating system to perform installation.

1. Windows
2. Linux

''')
def main():
    cmd=input("Enter the option for os selection :")
    if(cmd==str(1)):
        print("Installing required packages to run wallpaper crawler")
        sleep(1)
        windows()
    elif(cmd==str(2)):
        sleep(1)
        print("Installing required packages to run wallpaper crawler")
        linux()
    else:
        print("Select option between 1 and 2")
        main()
def windows():
    try:
        os.system('python -m pip install requests')
        os.system('python -m pip install bs4')
        os.system('python -m pip install lxml')
        sleep(1)
        print("All packages are installed successfully.")
        input("Press enter to continue.")
    except:
        print("Error in installation.")
def linux():
    try:
        os.system('python3 -m pip install requests')
        os.system('python3 -m pip install bs4')
        os.system('python3 -m pip install lxml')
        sleep(2)
        print("All packages are installed successfully.")
        input("Press enter to continue.")
    except:
        print("Error in installation.")

if __name__=="__main__":
    main()
