# Dealing with files and error/exception handling

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

# Second iteration:
# Your task is to read the data and display it as a list

# 3rd iteration
# Create a function to the same job DRY