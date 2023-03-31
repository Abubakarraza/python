# Doc String

# python docstring are the string literals that appear right after the definition of a function ,method,class,or modules

# Syntax:
# Doc string are defined just after the name of function or above the body of function otherwise it can't work it defined using '''''' triple string
# Example : 

def square(num):
    '''Takes a number and return the square of number'''
    print(num **2) 
square(2)

# Accessing doc string 

# you can access doc string using __doc__ in function
# Example :

print("Doc String:",square.__doc__)

# Note : Doc string which will not appear in output

