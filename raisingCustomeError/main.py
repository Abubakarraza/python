# Raising Custom Error

# In python, we can raise custom errors by using the raise keyword

number = (input("Enter number b/w 2 to 8:"))

if number == "quit":
    print("quit program")
elif int(number) < 2 or int(number) > 8:
    raise ValueError("Invalid Number")
else:
    print("number:",number)


# In the previous tutorial, we learned about different built-in exception in python and why it is important to handle exceptions. However, sometimes we may need to create our own custom exception that serve our purpose