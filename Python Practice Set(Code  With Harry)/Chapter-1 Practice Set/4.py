# Write a python program to print the contents of a directory using the os module. 
import os

def list_directory_contents(path='.'):
    try:
        # List all files and directories in the specified path
        contents = os.listdir(path)
        print(f"Contents of '{path}':")
        for item in contents:
            print(item)
    except Exception as e:
        print(f"An error occurred: {e}")