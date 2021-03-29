# Dealing with files and Exception Handling in Python

## We have `try`, `except`, `raise` and `finally` as our code block to handle the error or an exceptions
- `try`: attempt to run the code. Lets you test a block of code for errors.
- `except`: execute if ErrorType is thrown. Lets you handle the error.
- `finally`: executes after the try and except no matter the outcome. Lets you execute code, regardless of the result of the try- and except blocks.
- `raise`: manually raises an error. As a developer you can choose to throw an exception if a condition occurs. ErrorType("The message you want to show.")

### To understand the concept easily:
- Each block of code works as an if, elif, else block.
````python
# There is a built in method in python called open("")

# Try to open a file. This file does exist.
try:
    file = open("orders.text")
    print("File is found.")
except FileNotFoundError as errmsg:
    print("File not found." + str(errmsg))
    #raise
finally:
    print("After opening, your task is to read the data and display it as a list.")
````
- Please ensure to create an orders.text if does not exist.
  
### File creation and modification
- Different modes to operate with a file:

| Mode |Description|
| :----: |:---- |
|'r' |This is the default mode. It Opens file for reading. |
|'w' |This Mode Opens file for writing. If file does not exist, it creates a new file. If file exists it truncates the file.|
|'x' |Creates a new file. If file already exists, the operation fails.|
|'a' |Open file in append mode. If file does not exist, it creates a new file.|
|'t' |This is the default mode. It opens in text mode.|
|'b' |This opens in binary mode.
|'+' |This will open a file for reading and writing (updating)|

It is worth noting that the `+` operator can be used with

- Example 1 - Read data from a file and print it:
````python
def open_read_display(name):
    try:
        file = open(name)
        print("File is found and opened.")
    except FileNotFoundError as errmsg:
        print("File not found." + str(errmsg))
        raise
    finally:
        print("Here is the text...")
        for line in file.readlines():
            print(line.rstrip('\n'))
        file.close()

open_read_display("orders.text")
````
- Example 2 - Write an additional line to the file:
````python
def write_file(name, item):
    try:
        file = open(name, "w")
        print("File is found and we will process to write.")
    except FileNotFoundError as errmsg:
        print("File not found." + str(errmsg))
        raise
    finally:
        file.write(item + "\n")
        print("List of items updated.")
        file.close()

write_file("orders.text", "Sandwich")
````
### CRUD

CRUD is the acronym for "Create, Read, Update and Delete", which is used to refer to the basic functions in databases or the persistence layer in a software. Basically, the CRUD Operations in Python is written in python programming language and MySQL database.

- `create`: 
- `read`:
- `update`:
- `delete`:
