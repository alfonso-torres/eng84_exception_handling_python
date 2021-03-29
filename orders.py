# Dealing with files and error/exception handling

# There is a built in method in python called open("")
# file = open("orders.text") # Looks for the file called orders.text

# Open a file that exists
#try:
#    file = open("orders.text")
#    print("File is found.")
#except FileNotFoundError as errmsg:
#    print("The above block of code was not executed." + str(errmsg))
#    #raise
#finally:
#    print("Your task is to read the data and display it as a list.")

# Open a file that does not exist
#    file = open("ordeeeers.text")
#    print("File is found.")
#except FileNotFoundError as errmsg:
#    print("File not found." + str(errmsg))
#    #raise
#finally:
#    print("Your task is to read the data and display it as a list.")

# Second iteration:
# Your task is to read the data and display it as a list
#file1 = open("orders.text")
#print(file1.read())
#file1.close()

# 3rd iteration
# Create a function to read the data and display it as a list (to the same job as before) DRY
def open_read_display(name):
    try:
        file = open(name) # Open the file
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

# -----GOOD EXAMPLE-----
#def open_using_with_and_print(file):
#    try:
#        with open(file, "r") as file:
#            for line in file.readlines():
#                print(line.rstrip('\n'))
#    except FileNotFoundError:
#        print("file cannot be found or directory is incorrect, please check the details provided")
#        raise
#    finally:
#        print("\nPlease chose the items from the list  and enjoy your HAPPY MEAL")
#open_using_with_and_print("orders.text")

# Create a function to write an additional line to orders.text
def write_file(name, item):
    try:
        file = open(name, "w") # Open the file with the mode of written
        print("File is found and we will process to write.")
    except FileNotFoundError as errmsg:
        print("File not found." + str(errmsg))
        raise
    finally:
        file.write(item + "\n")
        print("List of items updated.")
        file.close()

write_file("orders.text", "Sandwich")

# -----GOOD EXAMPLE-----
#def write_to_file(file, order_item):
#    try:
#        with open(file, "w") as file:
#            file.write(order_item + '\n')
#    except FileNotFoundError:
#        print("file cannot be found or directory is incorrect, please check the details provided")
#        raise

#write_to_file("order.txt", "Ice Cream")
