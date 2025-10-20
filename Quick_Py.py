print("Starting Quick_Py.py for quick Python Revision...")
# BASICS
print("-------------------BASICS--------------------")
print("Python is an interpreted, high-level, general-purpose programming language.")
print("It supports multiple programming paradigms, including procedural, object-oriented, and functional programming.")
print("Python has a large standard library that provides many useful modules and functions.")
print("Python uses indentation to define blocks of code, making it easy to read and understand.")
print("Python is dynamically typed, meaning you don't need to declare variable types explicitly.")
print("Python has a large and active community, which contributes to its extensive ecosystem of libraries and frameworks.")
print('-'*40)
# This script is intended for quick revision of Python concepts.
print("Let's start with some basic concepts!")
print('-'*40)
print("1. Variables and Data Types")
print("2. Control Structures")
print("3. Functions")
print("4. Modules and Packages")
print("5. File I/O")
print('-'*40)
# Variables and Data Types
print("In Python, variables are created when you assign a value to them.")
print("Example:")
print("x = 5")
print("y = 'Hello'")
print("Data types include:")
print("- Integers")
print("- Floats")
print("- Strings")
print("- Lists")
print("- Dictionaries")
print('-'*40)
# Lists
print("Lists are ordered collections of items.")
print("Example:")
my_list = [1, 2, 3, 4, 5]
print("You can access elements by their index:")
print(my_list[0])   # Output: 1
my_list.append(6)  # Adding an element
print("Updated List:", my_list)
my_list.remove(3)  # Removing an element
print("List after removal:", my_list)
print("POPping last element:", my_list.pop())
print("List after POP:", my_list)
print('Length of List:', len(my_list)) # Length of the list
print('my_list now contains:', my_list)
my_list.sort()  # Sorting the list
my_list.reverse()  # Reversing the list
print("List after reverse:", my_list)
print("Slicing the list:", my_list[0:2])
print("Iterating through the list:")
# When you copy a list, you create a new list in memory.
my_list2 = my_list.copy()
my_list2.extend([7, 8, 9])
print("Extended List:", my_list2)
# When you assign one list to another, both refer to the same list in memory.
my_list3 = my_list2 
my_list3.append(11)
print("List after adding 11:", my_list3)
my_list2
print('-'*40)
# Tuples
print("Tuples are similar to lists but are immutable (cannot be changed).")
print("Example:")
my_tuple = (1, 2, 3)
print("You can access elements by their index:")
print(my_tuple[0])  # Output: 1
print("Tuples are immutable, so you cannot add or remove elements.")
print("However, you can concatenate tuples:")
new_tuple = my_tuple + (4, 5)
print("New Tuple:", new_tuple)
print("You can also unpack tuples:")
a, b, c, d, e = my_tuple + (4, 5)
print("Unpacked Values:", a, b, c, d, e)
my_tuple2 = (6, 7, 8)
combined_tuple = my_tuple + my_tuple2
print("Combined Tuple:", combined_tuple)
print("Length of Tuple:", len(combined_tuple))
print("Iterating through the tuple:")
my_tuple3 = my_tuple2 + (9, 10)
print("Extended Tuple:", my_tuple3)
print('-'*40)
# Dictionaries
print("Dictionaries are collections of key-value pairs.")
print("Example:")
my_dict = {'name': 'Alice', 'age': 25}
print("Accessing values by key:")
print(my_dict['name'])  # Output: Alice
my_dict['age'] = 26  # Updating a value
print("Updated Dictionary:", my_dict)
my_dict['city'] = 'New York'  # Adding a new key-value pair
print("Dictionary after adding city:", my_dict)
del my_dict['age']  # Removing a key-value pair
print("Dictionary after deleting age:", my_dict)
print("Iterating through the dictionary:")
for key, value in my_dict.items():
    print(f"{key}: {value}")
print("Dictionary Keys:", my_dict.keys())
print("Dictionary Values:", my_dict.values())
print("Length of Dictionary:", len(my_dict))

Students = {
   'Name' : 'Alice',
   'Age' : 25,
   'City' : 'New York'
}
print("Students Dictionary:", Students)

Players = { 
           "Game" : "Football",
              "Team" : "Real Madrid",
                "Country" : "Spain",
                "Level" : 5,
                "Ground" : []
}

print("Players Dictionary:", Players)
print("Accessing Team:", Players["Team"])
Players["Level"] +=1
print("Updated Level:", Players["Level"])
print("All Keys:", Players.keys())
print("All Values:", Players.values())
print("Length of Players Dictionary:", len(Players))
Players["Ground"].append("Santiago Bernabeu")
print("Updated Ground List:", Players["Ground"])
print('-'*40)
# Control Structures
print("Control structures include if-else statements and loops.")
print("Example of if-else:")
Code = 0
if Code == 0:
    print("Code is zero")
elif Code == 1:
    print("Code is one")
else:
    print("Code is something else")

# Example of nested if-else
marks = 1111
if marks <= 100:
    if marks >= 90:
        print("Grade: A")
    elif marks >= 80:
        print("Grade: B")
    elif marks >= 70:
        print("Grade: C")
    elif marks >= 60:
        print("Grade: D")
    else:
        print("Grade: F")
else:
    print("Invalid marks") 

container = -1
if container > 0:
    print("Container is not empty")
    if container > 10:
        print("Container is overfilled")
    else:
        print("Container has some space left")
else:
    print("Container is empty")
    
n = 2
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")
    
print("Example of while loop:")

count = 0
while count < 5:
    print(count)
    count += 1

n = 2
x = 1
while x <= 10:
    print(f"{n} x {x} = {n*x}")
    x += 1

n = 5

x = 10
while x >= 1:
    print(f"{n} x {x} = {n*x}")
    x -= 1

# Break and Continue
print("Example of Break:")
for i in range(5):
    if i == 3:
        break
    print(i)

print("Example of Continue:")
for i in range(5):
    if i == 2:
        continue
    print(i)
   
   
condition = -4>0
if condition == True:
    print("A")
    print("B")
    print("C")
    print('D')
else:
    print("Code error") 
    
Name = ['Vicky', 'Rohit', 'Aman', 'Vishal', 'Golu', 'Tejashwi']
x = ['Vicky', 'Rohit', 'Aman', 'Vishal', 'Golu', 'Tejashwi']
if x ==  Name:
    print("Your're in heart")
else:
    print("Enemy")
    
def greet():
    Name = "V"
    print(f"Good Morning {Name}")
greet()

x = 30
y = 20
if x > y:
    print("X is greater than Y")
else:
    print("Y is greater than X")

x = 0
y = -1
if x > 0 and y > 0:
    print("Both are positive")
elif x > 0 or y > 0:
    print("One is positive")
else:
    print("Both are non-positive")
    
x = 25
y = 50
if x > 20 and y < 100:
    print("X is greater than 20 and Y is less than 100")
else:
    print("Condition not met")
    
x = 10
if x!= 0:
    print("X is matching")
else:
    print("X is not matching")



X_color = "Orange"
if X_color == "Red":
    print("Stop")
elif X_color == "Yellow":
    print("Get Ready") 
elif X_color == "Green":
    print("Go")
else:
    print("Wrong Color")
    

print("Example of Nested If-Else:").lower()


#Fibonacci Series
a = 0
b = 1
c = 2 
for i in range(100):
    c = a + b
    a = b
    b = c
    print(c, end=' ')
    

def add_no(a, b):
    return a + b
x = add_no(2, 10)
print("Sum is:", x)
print("\nSum is:", add_no(5, 10))

print('-'*40)

#Built-in Functions
print("Built-in Functions:")
print(dir(str))
print(dir(list))
print(dir(dict()))

for i in dir(str):
    print(i)
    
help(type)
help(str)


text = f"{a}, {b}, {c}"
a = "Hello"
b = "World"
c = 2024
print(text)

# List Methods  also use in Tuple, Dictionary, Set, String
x = [1,2,3,4,6,7, 8,5]
x.index(3)
x.count(3)
x.sort()
x.reverse()
x.append(9)
x[x.index(3)] = 10
x.remove(4)
x[x.index(2)] = 20 # This will give error as list has no replace method
x.pop(0)
x.insert(2, 15)
print(x)

print("-+"*50)

print("Lower, Upper, Title, Capitalize, Swapcase")
text = "hello world"
print(text.lower())
print(text.upper())
print(text.title())
print(text.capitalize())
print(text.swapcase())

print("Find, Index, Replace, Count")
text = "hello world, welcome to the world of python"
print(text.find("world"))  # Returns the index of the first occurrence
print(text.index("world")) # Returns the index of the first occurrence
print(text.replace("world", "universe")) # Replaces all occurrences
print(text.count("world")) # Counts occurrences of substring
print("Split and Join")

text = "hello world, welcome to the world of python"
print(text.split(" "))  # Splits the string into a list
print(" ".join(["hello", "world"]))  # Joins a list into a string

t = "   She looks so Cute    "
print(t.strip())  # Removes leading and trailing whitespace

w = "HEllo WoRLd"
print('_'.join(w))  # Joins each character with '_'


print("Strip, Lstrip, Rstrip")
text = "   hello world   "
print(text.strip())  # Removes leading and trailing whitespace
print(text.lstrip()) # Removes leading whitespace
print(text.rstrip()) # Removes trailing whitespace

print("Startswith, Endswith, Isalpha, Isdigit, Isalnum")
text = "Hello123"
print(text.startswith("Hello"))  # Checks if string starts with substring
print(text.endswith("123"))      # Checks if string ends with substring
print(text.isalpha())            # Checks if all characters are alphabetic
print(text.isdigit())            # Checks if all characters are digits
print(text.isalnum())            # Checks if all characters are alphanumeric
print("Length, Max, Min, Sum")
print(len(text))                 # Length of the string
print(max(text))                 # Max character (based on ASCII value)
print(min(text))                 # Min character (based on ASCII value)
print(sum(map(ord, text)))      # Sum of ASCII values

print("Type, Id, Int, Str, Float, List, Tuple, Dict")
print(type(text))                # Type of the variable
print(id(text))                  # Memory address of the variable
print(int("123"))                # Converts string to integer
print(str(123))                  # Converts integer to string
print(float("123.45"))           # Converts string to float
print(list("hello"))             # Converts string to list of characters
print(tuple("hello"))            # Converts string to tuple of characters
print(dict(a=1, b=2))            # Creates a dictionary from keyword arguments

print('-'*40)

# writing to a file
file = open("sample.txt", "w")
file.write("Hello, World!\nI'm learning Python file handling.\n"
           "This is the third line.\n"
           "Fourth line here.\n"
           "Fifth line.\n")
file.close()

#reading a file
file = open("sample.txt", "r")
content = file.read()   
print(content)
file.close()

#appending to a file
file = open("sample.txt", "a")
file.write("This is an appended line.\n")
file.close()

print("Reading file line by line:")
file = open("sample.txt", "r")
for line in file:
    print(line, end='')  # end='' to avoid double newlines
file.close()


print('-'*40)

import os
file = open("sample.txt", "w")
file.write("numpy\npandas\nmatplotlib\nseaborn\nscikit-learn\nscipy\nstatsmodels\nopenpyxl\njupyter\n")
file.close()

#pip install -r sample.txt



#Automate Excel with Python
import openpyxl                      # Imports the library
filename = 'sample.xlsx'            # Sets the desired filename
wb = openpyxl.Workbook()            # Creates a new workbook object
print(wb)                           # Prints the workbook object reference
ws = wb.active                     # Gets the active worksheet
print(ws) 
ws = wb['sheet81']  
all_ws = wb.sheetnames
print(all_ws)                       # Prints the active worksheet object reference


import logging
logging.debug("This is a debug message")
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")

import os
from pathlib import Path

# Define the path to the Downloads folder
path_downloads = Path.home() / "Downloads"
print(f"Scanning: {path_downloads}")

# Define file categories and their associated extensions
categories = {
    "Documents": ['doc', 'docx', 'pdf', 'txt', 'xls', 'xlsx', 'ppt', 'pptx'],
    "Pictures": ['jpg', 'jpeg', 'png', 'gif', 'bmp'],
    "Music": ['mp3', 'wav', 'aac', 'flac'],
    "Videos": ['mp4', 'mkv', 'avi', 'mov'],
    "Archives": ['zip', 'rar', '7z'],
    "Code": ['py', 'js', 'html', 'css', 'ipynb']
}

# Loop through each file in Downloads
for file in os.listdir(path_downloads):
    file_path = path_downloads / file

    # Skip directories and hidden/system files
    if not file_path.is_file() or file.startswith('.'):
        continue

    # Skip files without extensions
    if '.' not in file:
        continue

    file_extension = file.split('.')[-1].lower()
    sorting_cat = None

    # Match file extension to category
    for cat, extensions in categories.items():
        if file_extension in extensions:
            sorting_cat = cat
            print(f"Matched: {file} → {cat}")
            break

    # Move file to its category folder
    if sorting_cat:
        category_path = path_downloads / sorting_cat
        category_path.mkdir(exist_ok=True)
        new_file_path = category_path / file
        file_path.rename(new_file_path)
        print(f"Moved: {file} → {sorting_cat}/")
    else:
        print(f"No category for: {file}")
