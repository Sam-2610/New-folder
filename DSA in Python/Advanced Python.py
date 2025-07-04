# Warlus Operator

if (n := len([1, 2, 3, 4, 5])) > 3: 
    print(f"List is too long ({n} elements, expected <= 3)")

# Type Definations


age: int = 25 
 
def greeting(name: str) -> str: 
    return f"Hello, {name}!" 

print(greeting("Alice")) 

# Advanced Type Hints

from typing import List, Tuple, Dict, Union 

numbers: List[int] = [1, 2, 3, 4, 5] 

person: Tuple[str, int] = ("Alice", 30) 

scores: Dict[str, int] = {"Alice": 90, "Bob": 85} 
 
identifier: Union[int, str] = "ID123" 
identifier = 12345  

# Match Status

def http_status(status): 
    match status: 
        case 200: 
            return "OK" 
        case 404: 
            return "Not Found" 
        case 500: 
            return "Internal Server Error" 
        case _: 
            return "Unknown status" 
    # Usage 
print(http_status(200))  # Output: OK 
print(http_status(404))  # Output: Not Found 
print(http_status(500))  # Output: Internal Server Error 
print(http_status(403))  # Output: Unknown status 

# DICTIONARY MERGE & UPDATE OPERATORS 

dict1 = {'a': 1, 'b': 2} 
dict2 = {'b': 3, 'c': 4} 
merged = dict1 | dict2 
print(merged)  # Output: {'a': 1, 'b': 3, 'c': 4} 

# File Opening

with ( 
open('file1.txt') as f1, 
open('file2.txt') as f2 
): 

# ENUMERATE FUNCTION IN PYTHON

list1 = ['a', 'b', 'c']
for i, item in enumerate(list1):
    print(i, item)

# LIST COMPREHENSIONS

list1 = [1,7,12,11,22,] 
list2 = [i for item in list 1 if item > 8]

