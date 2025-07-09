"""  Write a python program to rename a file to “renamed_by_ python.txt. """
import os

# Original file name (make sure it exists in the same folder)
original_file = "this.txt"
new_name = "renamed_by_python.txt"

try:
    os.rename(original_file, new_name)
    print(f"File renamed to '{new_name}' successfully.")
except FileNotFoundError:
    print(f"The file '{original_file}' does not exist.")
except Exception as e:
    print("Error:", e)
