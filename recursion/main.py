# Recursion 

# Recursion is the process of defining something in terms of itself

# A Physical world example would be to place two parallel mirrors facing each other. Any object in between them would be reflected recursively

# Python Recursive function

# In python, we know that a function can call other functions. Is is even possible for the function to call itself . These types of construct are termed ad recursive function

# Example : Factorial of any function 
def factorial (n):
    if(n==0 or n==1):
        return 1
    else:
        return n * factorial(n-1)
num=7
print("number:",num)
print("Factorial:",factorial(num))