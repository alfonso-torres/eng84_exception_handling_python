# Dealing with files and Exception Handling in Python

## We have `try`, `except`, `raise` and `finally` as our code block to handle the error or an exceptions

### To understand the concept easily:
- Each block of code works as an if, elif, else block.
````python
# There is a built in method in python called open("")
# file = open("orders.text") # Looks for the file called orders.text

try:
    file = open("orders.text")
    print("File is found.")
except FileNotFoundError as errmsg:
    print("The above block of code was not executed." + str(errmsg))
    #raise
finally:
    print("Your task is to read the data and display it as a list.")
````
- Please ensure to create an orders.text if does not exist.
- Different modes to do with a file:

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