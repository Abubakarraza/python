
# Exception Handling

# Exception handling is the process of responding to unwanted or unexpected events when a computer program runs. Exception handling deals with these events to avoid the program or system crashing, and without this process, exception would disrupt the normal operation of a program

# Exception in python

# python has many built in exception that are raised when your program encounter an error (something in the program goes wrong). when these exception occur , the python interpreter stops the current process and passes it to the calling process until it is handled . If not handled, the program will crash.


# Python try ...except

# try ...except blocks are used in python to handle errors and exceptions. The code is try block runs when there is no error. If the try block catches the error, then the except block is executed.

# just like (try and catch in javascript)

# Syntax

# try:
    # statement which could generate exception
# except: 
    # solution of generated exception


# Example 1: 

try:
    num = int(input("Enter any number:"))
    print(num)
except Exception as e:
    print("Error:",e)    

# In these case if user type string instead of integer it raise error because it expect int but it get string to solve this we use try except

# Example 2 :

# print any table 

try:
    no = int(input("Enter number for table:"))
    for i in range(1,11):
        print(f"{no} * {i} = {no * i}")
except Exception as e:
    print("Error:",e)        


# There are many type error handler in python we discuss it later


# Finally Clause 

# The finally code block is also a part of exception handling. When we handle exception using the try and except block , we can include a finally block at the end. The finally block is always executed, so it generally used for doing the concluding tasks like closing file resources or closing database connection or may be ending the program execution with a delightful message



# Syntax 

# try :
    #    statement which could generate exception
# except: 
    #  solution of generated exception
# finally: 
         # block of code which is going execute in any case 


# Example :
try:
    num = int(input("Enter an integer: "))
except ValueError:
    print("Number entered is not an integer.")
else:
    print("Integer Accepted.")
finally:
    print("This block is always executed.")
